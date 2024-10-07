#Programa: LAB02_EJER_15.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 30/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code




def suma(a: 'parametro 1' , b: 'parametro 2' ) -> 'retorno': 
    return a + b

print(suma.__annotations__)
#Salida:
#{'a': 'parametro 1', 
# #b': 'parametro 2', 
# #'return': 'retorno"}