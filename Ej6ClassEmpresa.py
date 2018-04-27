from Ej6ClassVehiculo import vehiculo

class empresa(object):

    nombre = None

    def __init__(self):

        self.Lista_autos = []
        self.Lista_camioneta = []


    def AgregarAutos(self, unAuto):

        self.Lista_autos.append(unAuto)

    def AgregarCamioneta(self, unaCamioneta):

        self.Lista_camioneta.append(unaCamioneta)