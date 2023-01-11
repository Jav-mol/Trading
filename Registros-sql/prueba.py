import psycopg2
from datetime import datetime, date

conexion = psycopg2.connect(
    user = 'javi',
    password = 'alumno',
    host = 'localhost',
    port = '5432',
    database = 'trading'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE trades SET derivado = %s, margen = %s, apalancamiento = %s, fecha_apertura = %s, fecha_cierre = %s, tarifa = %s, ganancia = %s WHERE id_trade = %s'
            #sentencia = 'INSERT INTO trades2 (derivado, margen, apalancamiento, fecha_apertura, fecha_cierre, tarifa, ganancia) SELECT derivado, margen, apalancamiento, fecha_apertura, fecha_cierre, tarifa, ganancia FROM trades'
            
            sentencia = 'UPDATE trades SET trade_tipo = %s WHERE id_trade IN %s  '
            valores = ('Short',(1,2,3,4,5,6,7,8))
            
            #id = input('Ingrese el ID del trade a medificar: ')
            #
            #der = input('Derivado: ')
            #mar = float(input('Margen: '))
            #apa = int(input('Apalancamiento: x'))
            #fec_a = input('Fecha Apertura: ')
            #fec_c = input('Fecha Cierre: ')            
            #tar = input('Tarifa: $')
            #gan = float(input('Ganancia: $'))
            #
            #valores = (der,mar,apa,fec_a,fec_c,tar,gan,id)
            cursor.execute(sentencia, valores)
            
            #registros = cursor.fetchall()
            
            #print(type(registros))
            
            

except Exception as e:
    print(f'Ocurrio un error tipo: {e}')
finally:
    conexion.close()