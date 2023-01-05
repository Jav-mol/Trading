import psycopg2 as pg

conexion = pg.connect(
    user = 'javi',
    password = 'alumno',
    host = '127.0.0.1',
    port = '5432', 
    database = 'trading'
)

class Registros:
    @classmethod
    def agregar_trade(self,derivado, margen, trade_tipo, apalancamiento,fecha_apertura,fecha_cierre,tarifa,ganancia) -> None:
        self.derivado = derivado
        self.margen = float(margen)
        self.trade_tipo = trade_tipo
        self.apalancamiento = int(apalancamiento)
        self.fecha_apertura = fecha_apertura
        self.fecha_cierre = fecha_cierre
        self.tarifa = float(tarifa)
        self.ganancia = float(ganancia)
        try:
            with conexion:
                with conexion.cursor() as cursor:

                    sentencia = 'INSERT INTO trades (derivado, margen, trade_tipo, apalancamiento,fecha_apertura,fecha_cierre,tarifa,ganancia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

                    valores = (self.derivado),(self.margen),(self.trade_tipo),(self.apalancamiento),(self.fecha_apertura),(self.fecha_cierre),(self.tarifa),(self.ganancia)

                    cursor.execute(sentencia, valores)
                    
            print('Trade agregado ;)')
        except Exception as e:
            print(f'Ocurrio un error al iniciar la clase. De tipo: {e}')
    
    @staticmethod
    def listar_registro():
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'SELECT * FROM  trades ORDER BY id_trade'

                    cursor.execute(sentencia)

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
            print(f'Ocurrio un error en "Listar Registros". De tipo: {e}')

    @staticmethod
    def recuento_ganancias():
        try:
            with conexion:
                with conexion.cursor() as cursor:
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
            print(f'Ocurrio un error en "Recuento de Ganancias". De tipo: {e}')
    
    @staticmethod
    def recuento_tarifas():
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    suma = 0
                    sentencia = 'SELECT * FROM trades'
                    
                    cursor.execute(sentencia)
                    
                    registros = cursor.fetchall()
                    
                    for i in registros:
                        suma += i[7]
                    print(f'El gasto en tarifas acumulado es de \n=>${suma:.2f}')
        except Exception as e:
            print(f'Ocurrio un error en "Recuento de Tarifas". De tipo: {e}')

    @staticmethod
    def actualizar_trade():
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'UPDATE trades SET derivado = %s, margen = %s, trade_tipo = %s, apalancamiento = %s, fecha_apertura = %s, fecha_cierre = %s, tarifa = %s, ganancia = %s WHERE id_trade = %s'
                    
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
                    cursor.execute(sentencia,valores)
           
        except Exception as e:
            print(f'Ocurrio un error en "Actualizar Trade". De tipo: {e}')
