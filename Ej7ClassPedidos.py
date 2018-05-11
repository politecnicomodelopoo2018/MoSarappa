from Ej7ClassPlato import plato
from Ej7ClassPersonas import profesores



class pedidos (object):

    fecha_creacion = None
    plato = None
    persona = None
    hora_entrega = None
    SeEntregoONo = None
    Codigo = None
    precio_final = None

    def __init__(self,fecha_creacion, plato, persona, hora_entrega, SeEntregoONo, Codigo, precio_final):

        self.fecha_creacion = fecha_creacion
        self.plato = plato
        self.persona = persona
        self.hora_entrega = hora_entrega
        self.SeEntregoONo = SeEntregoONo
        self.Codigo = Codigo
        self.precio_final = precio_final
        self.Lista_Alumnos = []
        self.Lista_Profesores = []

    def PrecioFinal (self):

        precio_final = (profesores.descuento/ 100) * plato.precio

        return precio_final





