class personas(object):
    nombre = None
    apellido = None

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class alumnos(personas):

    division = None

class profesores(personas):
    descuento = None

