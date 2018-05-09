from Ej6ClassVehiculo import vehiculo

class empresa(object):

    nombre = None

    def __init__(self, nombre):

        self.nombre = nombre
        self.Lista_autos = []
        self.Lista_camioneta = []


    def AgregarAutos(self, unAuto):

        self.Lista_autos.append(unAuto)

    def AgregarCamioneta(self, unaCamioneta):

        self.Lista_camioneta.append(unaCamioneta)

    def ListaPatentesAParaMostrar (self):
        listaPatenteA = []
        for item in self.Lista_autos:
            listaPatenteA.append(item.patente)
        return listaPatenteA

    def ListaPatentesCParaMostrar (self):
        listaPatenteC = []
        for item in self.Lista_camioneta:
            listaPatenteC.append(item.patente)
        return listaPatenteC

    def abrirPA(self):
        with open("PatentesA.txt", "w") as f:

            for item in self.ListaPatentesAParaMostrar():
                f.write(item + '\n')

    def abrirPC(self):


        with open("PatentesC.txt", "w") as f:

            for item in self.ListaPatentesCParaMostrar():
                f.write (item + '\n')

    def PatentesA (self):

        with open("PatentesA.txt", "r") as f:

            for line in f:
                print(line)

    def PatentesC (self):

        with open("PatentesC.txt", "r") as f:

            for line in f:
                print(line)                  