class vehiculo (object):

    patente = None
    cant_ruedas = None
    ano_fab = None

    def __init__(self,patente,cant_ruedas,ano_fab):

        self.patente = patente
        self.cant_ruedas = cant_ruedas
        self.ano_fab = ano_fab

class auto (vehiculo):

    descapotable = None

    def __init__(self, patente,cant_ruedas,ano_fab, descapotable):

        vehiculo.__init__(self, patente,cant_ruedas,ano_fab)

        self.descapotable = descapotable

class camioneta (vehiculo):

    cargaKg = None

    def __init__(self,patente, cant_ruedas, ano_fab, cargaKg):

        vehiculo.__init__(self, patente, cant_ruedas, ano_fab)

        self.cargaKg = cargaKg





