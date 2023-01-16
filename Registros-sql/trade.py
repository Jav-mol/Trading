import psycopg2 as ps
from logger import log

class Trade:
    def __init__(self,derivado = None, margen = None, trade_tipo = None, apalancamiento = None,fecha_apertura = None,fecha_cierre = None,tarifa = None,ganancia = None) -> None:
        self.derivado = derivado
        self.margen = float(margen)
        self.trade_tipo = trade_tipo
        self.apalancamiento = int(apalancamiento)
        self.fecha_apertura = fecha_apertura
        self.fecha_cierre = fecha_cierre
        self.tarifa = float(tarifa)
        self.ganancia = float(ganancia)