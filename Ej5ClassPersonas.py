class Persona(object):

    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self,nombre,apellido,fecha_de_nacimiento):

        self.nombre = nombre
        self.apellido=apellido
        self.fecha_nacimiento = fecha_de_nacimiento

class Artistas(Persona):

    pass

class Autores(Persona):

    nacionalidad = None

    def AgregarNacionalidad (self, nacionalidad):

        self.nacionalidad = nacionalidad

