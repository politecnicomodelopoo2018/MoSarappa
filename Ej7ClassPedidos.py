class pedidos (object):

    fecha_creacion = None
    plato = None
    persona = None
    hora_entrega = None
    SeEntregoONo = None
    Codigo = None

    def __init__(self,fecha_creacion, plato, persona, hora_entrega, SeEntregoONo):

        self.fecha_creacion = fecha_creacion
        self.plato = plato
        self.persona = persona
        self.hora_entrega = hora_entrega
        self.SeEntregoONo = SeEntregoONo

    def ModificarPlato (self, unPlato):

        self.plato = unPlato

    def AgregarPersona (self, unaPersona):

        self.persona = unaPersona


