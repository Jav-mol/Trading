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
    _cursor = None
    
    @classmethod
    def obtener_conexion(cls):
        try:
            if cls._conexion == None:
                cls._conexion = ps.connect(
                    database = cls._DATABASE,
                    user = cls._USER,
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._PORT
                )
                log.debug(f'Se ha obtenido la conexion: {cls._conexion}')
                return cls._conexion
            else:
                log.debug(f'Se ha retornado la conexion: {cls._conexion}')
                return cls._conexion
        except Exception as e:
            log.error(f'Ha ocurrido un error al obtener la conexion {e}')
            sys.exit()
    @classmethod
    def obtener_cursor(cls):
        try:
            if cls._cursor == None:
                cls._cursor = Conexion.obtener_conexion().cursor()
                log.debug(f'Se ha obtenido el cursor: {cls._cursor}')
                return cls._cursor
            else:
                log.debug(f'Se ha retornado el cursor: {cls._cursor}')
                return cls._cursor

        except Exception as e:
            log.error(f'Ha ocurrido un error al obtener el cursor: {e}')
            sys.exit()

if __name__ == '__main__':
    Conexion.obtener_cursor()