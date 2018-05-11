class personas(object):

    nombre = None
    apellido = None

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def descuento (self):
        return 0


class alumnos(personas):

    division = None

    def __init__(self, nombre, apellido, division):

        alumnos.__init__(self, nombre, apellido)

        self.division = division

class profesores(personas):

    descuento = None

    def __init__(self, nombre, apellido, descuento):

        profesores.__init__(self,nombre, apellido)

        self.descuento = descuento

    def descuento (self):

        return self.descuento