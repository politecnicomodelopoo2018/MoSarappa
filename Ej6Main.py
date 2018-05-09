from Ej6ClassVehiculo import auto
from Ej6ClassVehiculo import camioneta
from Ej6ClassEmpresa import empresa

vehiculo1 = auto("ABC342", "4", "2000", "descapotable")
vehiculo2 = auto("CDE234", "4", "1999", "no descapotable")
vehiculo3 = camioneta("RET345", "8", "1980", "no descapotable")
vehiculo4 = camioneta("ATR012", "4", "1995", "no descapotable")

empresa = empresa("Ford")


Auto1 = empresa.AgregarAutos(vehiculo1)
Auto2 = empresa.AgregarAutos(vehiculo2)

Auto3 = empresa.AgregarCamioneta(vehiculo3)
Auto4 = empresa.AgregarCamioneta(vehiculo4)


print(empresa.ListaPatentesAParaMostrar())

print(empresa.ListaPatentesCParaMostrar())

empresa.abrirPA()
empresa.abrirPC()


empresa.PatentesA()
empresa.PatentesC()
