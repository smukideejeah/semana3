# Nombre del programa: Class
# Numero de grupo de trabajo: 1
# Nombre de los programadores: Elvis Aguilar, Joseph Avilez 
# Fecha de elaboracion del programa: 23/09/24
# Version de PYTHON: 3.12
# #Nombre del IDE donde se trabajo el codigo: Visual Code

x = [10, 20, 30]
print(id(x)) # 4422423560
def funcion(entrada):
    entrada.append(40)
    print(id(entrada)) # 4422423560

    funcion(x)