from Ej7ClassPedidos import pedidos
import datetime

class Buffe (object):

    def __init__(self):

        self.List_Pedidos = []
        self.List_Platos = []
        self.List_Platos_Hoy = []

    def AgregarPlato(self, unPlato):

        self.List_Platos.append(unPlato)

    def AgregarPedidos (self, unPedido):

        self.List_Pedidos.append(unPedido)

    def BorrarPedidos (self, unPedido):

        for item in self.List_Pedidos:
            if item.Codigo == unPedido.Codigo:
                self.List_Pedidos.remove(unPedido)

    def BorrarPlato (self,unPlato):

        for item in self.List_Platos:
            if item.Codigo == unPlato.Codigo:
                self.List_Platos.remove(unPlato)


    def ModificarPedido (self, unPedido):

        for item in self.List_Pedidos:
            if item.Codigo == unPedido.Codigo:
                self.List_Pedidos.append(item.Codigo)

    def ModificarPlato (self, unPlato):

        for item in self.List_Platos:
            if item.Codigo == unPlato.Codigo:
                self.List_Platos.append(item.Codigo)

    def PlatosACocinarHoy (self, unPlato):

        for item in self.List_Platos:
            if item.fecha_creacion == datetime.datetime.now():

                self.List_Platos_Hoy.append(unPlato)

        return self.List_Platos_Hoy

