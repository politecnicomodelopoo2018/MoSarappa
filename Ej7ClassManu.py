from Ej7ClassPedidos import pedidos
from Ej7ClassPersonas import alumnos
from Ej7ClassPersonas import profesores
from Ej7ClassPlato import plato
from Ej7ClassBuffe import Buffe

class Menu (object) :

    opcion = None

    def __init__(self, opcion):

        self.opcion = opcion

    def Opcion (self,opcion):

        print("Eliga una Opcion:")

        print("|A1.Agregar Persona  |")
        print("|A2.Modificar Persona|")
        print("|A3.Eliminar Persona |")

        print("|B1.Agregar Plato    |")
        print("|B2.Modificar Plato  |")
        print("|B3.Eliminar Plato   |")

        print("|C1.Agregar Pedidos  |")
        print("|C2.Modificar Pedidos|")
        print("|C3.Eliminar Pedidos |")

        if opcion == "A1":

            print("|A1.Agregar Persona  |")





