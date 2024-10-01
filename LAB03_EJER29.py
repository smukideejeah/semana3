#Programa: LAB03_EJER_29.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 23/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Realizar un programa que permita calcular el salario de un trabajador, considerando las horas trabajadas y el salario por hora.

CCSS = 0.0933
AS = 0.05
EXTRA = 1.5;
TOTALHOUR = 192;

def salary(hours: int, normalSalary: int):
    extra = hours - TOTALHOUR;
    normalHours = hours
    extraSalary = 0;
    if extra > 0: 
        extraSalary = extra * (normalSalary * EXTRA)
        normalHours = hours - extra;

    normal = normalSalary * normalHours;
    bruto = normal + extraSalary;

    ccss = bruto * CCSS;
    asalary = bruto * AS;
    neto = bruto - ccss - asalary;
    return print(f"Salario Normal Bruto: {normal}\nSalario Extra Bruto ({extra} a 1.5x): {extraSalary}\n Salario Total bruto: {bruto}\nCCSS: {ccss}\nAsociacion: {asalary}\nNeto: {neto}");

inputHours = int(input("Ingrese las horas trabajadas: "));
inputSalary = int(input("Ingrese el salario por hora: "));

salary(inputHours, inputSalary);