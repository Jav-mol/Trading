from logger import log
from psycopg2 import pool
import psycopg2 as ps
import sys

class Conexion:
    _USER = 'javi'
    _PASSWORD = 'alumno'
    _DATABASE = 'trading'
    _HOST = 'localhost'
    _PORT = '5432'
    _MIN_CON = 1
    _MAX_CON = 3
    _pool = None
    
    @classmethod
    def obtener_pool(cls):
        try:
            if cls._pool == None:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    database = cls._DATABASE,
                    user = cls._USER,
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._PORT
                )
                log.debug(f'Se ha obtenido la conexion: {cls._pool}')
                return cls._pool
            else:
                log.debug(f'Se ha retornado la conexion: {cls._pool}')
                return cls._pool
        except Exception as e:
            log.error(f'Ha ocurrido un error al obtener la conexion {e}')
            sys.exit()
    @classmethod
    def obtener_conexion(cls):
        try:
            conexion = cls.obtener_pool().getconn()
            log.debug(f'Conexion obtenida correctamente: {conexion}')
            return conexion
        except Exception as e:
            log.error(f'Ha ocurrido un error al obtener la conexion: {e}')
            sys.exit()
    
    @classmethod
    def liberar_conexion(cls, conexion):
        try:
            cls.obtener_pool().putconn(conexion)
            log.debug(f'Conexion liberada correctamente: {conexion}')
        except Exception as e:
            log.error(f'Ha ocurrido un error al liberar la conexion: {e}')
            sys.exit()
    
    @classmethod
    def cerrar_conexion(cls):
        try:
            cls.obtener_pool().closeall()
            log.debug('Conexion cerrada correctamente')
        except Exception as e:
            log.error(f'Ha ocurrido un error al liberar la conexion: {e}')
            sys.exit()    
            
if __name__ == '__main__':
    try:
        c1 = Conexion.obtener_conexion()
        c2 = Conexion.obtener_conexion()
        c3 = Conexion.obtener_conexion()
        c4 = Conexion.obtener_conexion()
        #Conexion.liberar_conexion(c1)
        #Conexion.cerrar_conexion()
    except Exception as e:
        log.error(f'Ocurrio un error: {e}')