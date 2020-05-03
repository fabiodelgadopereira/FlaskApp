from flask import Flask, request, Blueprint
from flask_restful import Api, Resource, reqparse
from threading import Lock
import logging
from retry import retry
from tenacity import *
import pyodbc
from ..db import db_connection
from flask_jwt import JWT, jwt_required, current_identity

app = Flask (__name__)



# Implement singleton to avoid global objects
class ConnectionManager(object):    
    __instance = None
    __connection = None
    __lock = Lock()

    def __new__(cls):
        if ConnectionManager.__instance is None:
            ConnectionManager.__instance = object.__new__(cls)        
        return ConnectionManager.__instance       
    
    def __getConnection(self):
        if (self.__connection == None):
            self.__connection =   pyodbc.connect(db_connection)         
        return self.__connection

    def __removeConnection(self):
        self.__connection = None

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(10), retry=retry_if_exception_type(pyodbc.OperationalError), after=after_log(app.logger, logging.DEBUG))
    def executeQueryJSON(self, procedure, payload=None):
        result = {}  
        
        try:
            conn = self.__getConnection()
            
            cursor = conn.cursor()
              
            if payload:
                cursor.execute(f"EXEC {procedure} "+ payload)
            else:
                cursor.execute(f"EXEC {procedure} ")

            try:
                result = [dict((cursor.description[i][0], value) \
                    for i, value in enumerate(row)) for row in cursor.fetchall()]                           
            except:
                result = {}

            cursor.commit()  

        except pyodbc.OperationalError as e:            
            app.logger.error(f"{e.args[1]}")
            if e.args[0] == "08S01":
                # If there is a "Communication Link Failure" error, 
                # then connection must be removed
                # as it will be in an invalid state
                self.__removeConnection() 
                raise                        
        finally:
            cursor.close()
                            
        return result

class Queryable(Resource):
    def executeQueryJson(self, verb, payload=None):
        result = {}  
        procedure = f"[dbo].{verb}"
        result = ConnectionManager().executeQueryJSON(procedure, payload)
        return result

# Customer Class
class Customer(Queryable):

    @jwt_required()
    def get(self, customer_id):  
        result = self.executeQueryJson("[sp_Clientes_GetValueById]", customer_id)   
        return result, 200       
    
    @jwt_required()
    def put(self):
        ##todo
        result = {}
        return result, 202

    @jwt_required()
    def post(self):
        json_data = request.get_json(force=True)
        arg1 = json_data['Nome']
        arg2 = json_data['Cidade']
        arg3 = json_data['Email']
        arg4 = json_data['Sexo']
        commando = f" \'{arg1}\' , \'{arg2}\' , \'{arg3}\' , \'{arg4}\'"       
        result = self.executeQueryJson("[sp_Clientes_InsertValue]", commando)
        return result, 202

    @jwt_required()
    def delete(self, customer_id):       
        customer = {}
        customer["CustomerID"] = customer_id
        result = self.executeQueryJson("[sp_Clientes_DeleteValue]", customer)
        return result, 202

# Customers Class
class Customers(Queryable):
    @jwt_required()
    def get(self):     
        result = self.executeQueryJson("[sp_Clientes_GetAllValues]")   
        return result, 200
    

