#Programa: LAB03_EJER_23.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 23/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Realizar un programa que permita sumar dos números ingresados por el usuario.

def normalFunction(a, b):
    return a + b

print((lambda a, b: normalFunction(a, b))(2, 4))