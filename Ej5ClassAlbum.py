ºfrom Ej5ClassCancion import Cancion

class Album(object):

    Nombre = None

    def __init__(self,Nombre):

        self.nombre = Nombre

        self.Lista_Canciones = []

    def AgregarCancion (self, unaCancion):

        self.Lista_Canciones.append(unaCancion)

    def MostrarArtista (self, unArtista):

        self.Lista_de_artistas_album = []

        for itemCancion in self.Lista_Canciones:
            for itemArtista in itemCancion.Lista_Artistas:
                if itemArtista not in self.Lista_Artistas:

                    self.Lista_de_artistas_album.append(itemArtista)

        return self.Lista_de_artistas_album

    def ArtistaMasInfluyente (self)

        self.ListAux = []

        for itemCancion in self.Lista_Canciones:
            for itemArtista in itemCancion.Lista_Artistas:
                self.ListAux.append(itemArtista)

        ContTotal = 0
        ArtistaMasInfluente = None

        for item in self.ListAux:
            contador = 0
            for item2 in self.ListAux:
                if item == item2:
                    contador += 1
            if contador >= ContTotal:

                ContTotal = contador
                ArtistaMasInfluente = item

        return ArtistaMasInfluente


    def CancionesPorNacionalidad(self, nacionalidad):

        self.Lista_de_Autores_Nacionalidad = []

        for itemCancion in self.Lista_Canciones:
            for itemAutor in itemCancion.Lista_Autores:
                if itemAutor.nacionalidad == nacionalidad:
                    self.Lista_de_Autores_Nacionalidad.append(itemAutor)

        return self.Lista_de_Autores_Nacionalidad