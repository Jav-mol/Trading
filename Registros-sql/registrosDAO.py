from logger import log
from cursor_pool import CursorDelPool
from trade import *
import sys

class RegistrosDAO:
    _INSERT = 'INSERT INTO trades (derivado, margen, trade_tipo, apalancamiento,fecha_apertura,fecha_cierre,tarifa,ganancia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    _SELECT = 'SELECT * FROM  trades ORDER BY id_trade'
    _UPDATE = 'UPDATE trades SET derivado = %s, margen = %s, trade_tipo = %s, apalancamiento = %s, fecha_apertura = %s, fecha_cierre = %s, tarifa = %s, ganancia = %s WHERE id_trade = %s'
    
    @classmethod
    def agregar_trade(cls,trade) -> None:
        try:
            with CursorDelPool() as cursor:
                valores = (trade.derivado),(trade.margen),(trade.trade_tipo),(trade.apalancamiento),(trade.fecha_apertura),(trade.fecha_cierre),(trade.tarifa),(trade.ganancia)
                cursor.execute(cls._INSERT, valores)
            log.debug(f'Trade agregado: {trade} ;)')
            
        except Exception as e:
            log.error(f'Ocurrio un error al agregar un trade: {e}')
            sys.exit()
    
    @classmethod
    def listar_registro(cls):
        try:
            with CursorDelPool() as cursor:                    
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                for i in registros:
                    fecha = ((i[6])-(i[5]))
                    result = '{} days'.format(fecha.days)   
                    
                    print(f'''
id: {i[0]}
nombre: {i[1]}
margen: {(i[2]):.2f}
Tipo de trade: {i[3]}
apalancamiento: X{i[4]}
fecha de apertura: {i[5]}
fecha de cierre: {i[6]}
tiempo de operacion: {result}
tarifa: {i[7]}
ganancia: {i[8]} ''')
                        
        except Exception as e:
            log.error(f'Ocurrio un error en "Listar Registros". De tipo: {e}')
            sys.exit()
    @staticmethod
    def recuento_ganancias():
        try:
            with CursorDelPool() as cursor:
                suma = 0
                tarifa = 0
                sentencia = 'SELECT * FROM trades'
                
                cursor.execute(sentencia)
                
                registro = cursor.fetchall()
                
                for i in registro:
                    suma += i[8]
                    tarifa += i[7]
                suma += tarifa
                print(f'La Ganancia total acumulada es de \n=>${suma:.2f}')
                    
        except Exception as e:
            log.error(f'Ocurrio un error en "Recuento de Ganancias". De tipo: {e}')
            sys.exit()
            
    @staticmethod
    def recuento_tarifas():
        try:
            with CursorDelPool() as cursor:
                suma = 0
                sentencia = 'SELECT * FROM trades'
                
                cursor.execute(sentencia)
                
                registros = cursor.fetchall()
                
                for i in registros:
                    suma += i[7]
                print(f'El gasto en tarifas acumulado es de \n=>${suma:.2f}')
        except Exception as e:
            log.error(f'Ocurrio un error en "Recuento de Tarifas". De tipo: {e}')
            sys.exit()
            
    @classmethod
    def actualizar_trade(cls):
        try:
            with CursorDelPool() as cursor:                
                id = input('Ingrese el ID del trade a medificar: ')
                der = input('Derivado: ')
                mar = float(input('Margen: '))
                tra = input('Tipo de trade: ')
                apa = int(input('Apalancamiento: x'))
                fec_a = input('Fecha Apertura: ')
                fec_c = input('Fecha Cierre: ')            
                tar = input('Tarifa: $')
                gan = float(input('Ganancia: $'))
            
                valores = (der,mar,tra,apa,fec_a,fec_c,tar,gan,id)
                cursor.execute(cls._UPDATE,valores)
           
        except Exception as e:
            log.error(f'Ocurrio un error en "Actualizar Trade". De tipo: {e}')
            sys.exit()
            
if __name__ == '__main__':
    try:
        trade = Trade('Btc',10,'Short',3,'12-12-2023','12-12-2024',-0.1,1.2)
        RegistrosDAO.listar_registro()
    except Exception as e:
        log.error(f'Ocurrio un error en el metodo main: {e}')
        sys.exit()