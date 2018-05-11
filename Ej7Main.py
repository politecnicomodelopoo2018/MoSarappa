from Ej7ClassPedidos import pedidos
from Ej7ClassPersonas import personas

from Ej7ClassPersonas import alumnos
from Ej7ClassPersonas import profesores
from Ej7ClassPlato import plato
from Ej7ClassBuffe import Buffe


alumno1 = alumnos("Carlos", "Tevez", "4C")
alumno2 = alumnos("Mo", "Salah", "3C")
alumno3 = alumnos("Ramon", "Abila", "4A")

profesor1 = profesores("Schelloto", "Guillermo", "10")
profesor2 = profesores("Gallanto", "Marchelo", "5")
profesor3 = profesores("Bolan", "Ariel", "10")

Buffe = Buffe()

plato1 = plato("Fideos", "100", "BBB222")
plato2 = plato("Pizza", "50", "AAA111")

pedidos1 = pedidos("2018/05/11", "Fideos", "Tevez", "10:30", "Si", "BBB222", "150" )


Pedido1 = Buffe.AgregarPedidos(pedidos1)


print(pedidos.PrecioFinal())
