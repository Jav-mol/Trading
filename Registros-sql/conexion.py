from logger import log
import psycopg2 as ps
import sys

class Conexion:
    _USER = 'javi'
    _PASSWORD = 'alumno'
    _DATABASE = 'trading'
    _HOST = 'localhost'
    _PORT = '5432'
    _conexion = None
    
    @classmethod
    def obtener_conexion(cls):
        if cls._conexion == None:
            pass