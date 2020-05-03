import pyodbc
from os import path
from flask import current_app
import logging
from retry import retry
from threading import Lock
from tenacity import *

# Implementar singleton para evitar objetos globais
class ConnectionManager(object):    
    __instance = None
    __connection = None
    __lock = Lock()
    __logger = logging.getLogger(__name__)

    def __new__(cls):
        if ConnectionManager.__instance is None:
            ConnectionManager.__instance = object.__new__(cls)        
        return ConnectionManager.__instance       
    
    def __getConnection(self):
        if (self.__connection == None):
            self.__connection =   pyodbc.connect(current_app.config['SQLSERVER_CONNECTION_STRING'])         
        return self.__connection

    def __removeConnection(self):
        self.__connection = None

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(10), retry=retry_if_exception_type(pyodbc.OperationalError), after=after_log(__logger, logging.DEBUG))
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
                # Se houver um erro "Communication Link Failure",
                # então a conexão deve ser removida
                # como estará em um estado inválido 
                self.__removeConnection() 
                raise                        
        finally:
            cursor.close()
                            
        return result




