from registros import Registros as trading
from registros import conexion
from trade import Trade

menu = '''1-Agregar un Trade
2-Listar Registros
3-Recuento de Ganancias
4-Recuento de Tarifas
5-Actualizar Trade
=>'''
try:
    while True:
        print('='*35)
        print(' Registros de Trading '.center(35,'~'))
        opcion = input(menu)
        print('~'*35)
        if opcion == '1':
            try:
                print('='*35,'\n')
                print('='*35)
                print(' Agregar Trade '.center(35,'-'))
                derivado = input('Derivado: ')
                margen = float(input('Margen: '))
                tipo = input('Tipo de trade: ')
                apalancamiento = int(input('Apalancamiento: X'))
                fec_a = input('Fecha Apertura: ')
                fec_c = input('Fecha Cierre: ')            
                tarifa = input('Tarifa: $')
                ganancia = float(input('Ganancia: $'))
                trade = Trade(derivado,margen,tipo,apalancamiento,fec_a,fec_c,tarifa,ganancia)
                trading.agregar_trade(trade)
                print('~'*35)
                print('='*35,'\n')
            except Exception as e:
                print(f'Ocurrio un error en "Agregar Trade" {e}')
                print('~'*35)
                print('='*35,'\n')

        elif opcion == '2':
            print('='*35)
            trading.listar_registro()
            print('~'*35)
            print('='*35,'\n')


        elif opcion == '3':
            print('='*35,'\n')
            print('='*35)    
            print(' GANANCIAS '.center(35,'-'))
            trading.recuento_ganancias()
            print('~'*35)
            print('='*35,'\n')

        elif opcion == '4':
            print('='*35,'\n')
            print('='*35)    
            print(' TARIFAS '.center(35,'-'))
            trading.recuento_tarifas()
            print('~'*35)
            print('='*35,'\n')

        elif opcion == '5':
            try:
                print('='*35,'\n')
                print('='*35)            
                print(' Actualizar Trade '.center(35,'-'))
                trading.actualizar_trade()
                print('~'*35)
                print('='*35,'\n')
            except Exception as e:
                print(f'Ocurrio un error en "Actualizar Trade" {e}')
                print('~'*35)
                print('='*35,'\n')
        else:
            conexion.close()        
            print('='*35)    
            break
except Exception as e:
    print('Ocurrio un error en la interfaz. De tipo {e}')
