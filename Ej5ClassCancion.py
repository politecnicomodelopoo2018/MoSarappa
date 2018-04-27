from Ej5ClassPersonas import Artistas
from Ej5ClassPersonas import Autores

class Cancion(object):

    Titulo = None

    def __init__(self, Titulo):

        self.Titulo = Titulo

        self.Lista_Artistas = []
        self.Lista_Autores = []

    def AgregarArtista (self, unArtista):

        for item in self.Lista_Artistas:
            if item == unArtista:
                return False

        self.Lista_Artistas.append(unArtista)

    def AgregarAutor (self, unAutor):

        for item in self.Lista_Autores:
            if item == unAutor:
                return False

        self.Lista_Autores.append(unAutor)


    def ArtistaMasInfluyentePorCancion (self,nom):

        cont = 0
        for item in self.Lista_Artistas:
            if item.nombre == nom:
                cont += 1

        return