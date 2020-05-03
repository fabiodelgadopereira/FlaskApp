from flask import Flask, request, current_app
from flask_restful import  Resource
import pyodbc
from ..db import ConnectionManager
from flask_jwt import jwt_required

app = Flask (__name__)

class Queryable(Resource):
    def executeQueryJson(self, verb, payload=None):
        schema = current_app.config['SQLSERVER_SCHEMA'] 
        procedure = f"{schema}.{verb}"
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
    

