#Programa: LAB02_EJER_15.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 30/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

def filtrar_pares(salida: 'list'= [])-> 'list':
    return [i for i in salida if i%2==0]

print(filtrar_pares([1,2,3,4,5,6]))
#salida[2,4,6]