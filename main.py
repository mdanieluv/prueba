#Programa principal
from Ingreso_Datos import *
from Operciones_Basicas import Metodo_Imprimir_Basicas
from Operaciones_Avanzadas import Metodo_Imprimir_Avanzados
from Titulos import Metodo_Titulos

Metodo_Titulos("Bienvenidos a la Aplicación")
x=Metodo_LeerA()
y=Metodo_LeerB()
Metodo_Titulos("Operaciones Básicas")
Metodo_Imprimir_Basicas(x,y)
Metodo_Titulos("Operaciones Avanzadas")
z=Metodo_Leera()
Metodo_Imprimir_Avanzados(z)
Metodo_Titulos("Fin de la Aplicación")