from ClasePrograma import Programa

class radio (object):

    def __init__ (self)

        self.Lista_programas = []

    def setAgregarPrograma (self, UnProg):

        cont = 0

        for item in  self.Lista_programas:

            for item2 in self.Lista_horarios:

                for item3 in UnProg.ListaHorario:

                    if item2[0] == item3[0] and item2 [1] == item3 [1]:

                        cont += 1

        if cont == 0:

            self.Lista_programas.append (UnProg)


    def setMostrarPorgramacionPorDIA(self, nro_dia):

        self.Lista_Auxiliar = []

        for item in self.Lista_programas:

            for item2 in self.Lista_horarios:

                if item2[0] = nro_dia:

                    self.Lista_Auxiliar.append(item.nombre)

        return self.Lista_Auxiliar