from conexion import Conexion
from logger import log
import sys

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        try:
            log.debug(f'Iniciando el metodo: "__enter__"')
            self._conexion = Conexion.obtener_conexion()
            self._cursor = self._conexion.cursor()
            return self._cursor
        except Exception as e:
            log.error(f'Ocurrio un error en el metodo: "__enter__"')
            sys.exit()
    
    def __exit__(self, tipo_exception, valor_exception, detalle_exception):
        try:
            log.debug('Ejecutando el metodo: "__exit__"')
            if valor_exception:
                self._conexion.rollback()
                log.error(f'Ocurrio un error en el metodo: "__exit__": {tipo_exception}, {valor_exception}, {detalle_exception}')
                sys.exit()
            else:
                self._conexion.commit()
                log.debug('Commit de la transaccion')
            self._cursor.close()
            log.debug(f'Cursor cerrado correctamente: {self._cursor}')    
            Conexion.liberar_conexion(self._conexion)
        except Exception as e:
            log.error(f'Ocurrio un error en el metodo: "__exit__"')
            sys.exit()

if __name__=='__main__':
    try:
        with CursorDelPool() as cursor:
            print(cursor)
    except Exception as e:
        log.error(f'Ocurrio un error en el metodo: "__main__"')
        sys.exit()
    