class Programa (object):

    Nombre = None

    def __init__ (self):

        self.Lista_horarios = []
        self.Lista_conductores = []

    def Nom_Del_Programa (self, nom):

        self.nombre = nom


    def AgregarConductorALaLista(self, cond):
        cont = 0

        for item in self.Lista_conductores:

            if item == cond:

                cont += 1

        if cont == 0:

            self.Lista_conductores.append(cond)


    def AgregarHoriarioALaLista (self, nro_dia, nro_bloque):

        cont = 0

        for item in self.Lista_horarios:

            if item[1] == nro_bloque :

                cont += 1

        if cont == 0:

            self.Lista_horarios.append([nro_dia, nro_bloque])