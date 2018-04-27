class vehiculo (object):

    patente = None
    cant_ruedas = None
    año_fab = None

    def __init__(self,patente,cant_ruedas,año_fab):

        self.patente = patente
        self.cant_ruedas = cant_ruedas
        self.año_fab = año_fab

class auto (vehiculo):

    descapotable = None

class camioneta (vehiculo):

    cargaKg = None

