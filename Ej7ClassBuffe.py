class Buffe (object):

    def __init__(self):

        self.List_Pedidos = []
        self.List_Platos = []

    def AgregarPlato(self, unPlato):

        self.List_Platos.append(unPlato)

    def AgregarPedidos (self, unPedido):

        self.List_Pedidos.append(unPedido)

    def BorrarPedidos (self, unPedido):

        for item in self.List_Pedidos:
            if item.Codigo == unPedido.Codigo:
                self.List_Pedidos.remove(unPedido)


    def ModificarPedido (self, unPedido):

        for item in self.List_Pedidos:
            if item.Codigo == unPedido.Codigo:
                self.List_Pedidos.append(item.Codigo)
