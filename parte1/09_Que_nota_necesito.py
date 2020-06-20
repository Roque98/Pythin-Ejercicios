"""
Qué nota necesito
    Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
    El promedio del ramo se calcula con la siguiente formula.

    NC = (c1 + c2 + c3) / 3
    NF = NC * 0.7  + NL *.3

    Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.

    Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, 
    y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.


Ejemplo:
    Ingrese nota certamen 1: 45
    Ingrese nota certamen 2: 55
    Ingrese nota laboratorio: 65
    Necesita nota 72 en el certamen 3
"""

"""
ANALISIS

si:
    NF = NC * 0.7  + NL *.3
entonces:
    NF - (NL *.3) = NC * 0.7
    (NF - (NL *.3)) /.7 = NC 
    NC = (NF - (NL *.3)) /.7


Si:
    NC = (c1 + c2 + c3) / 3
entonces:
    NC*3 = c1 + c2 + c3
    NC*3 - (C1 + c2) = c3
    c3 = NC*3 - (c1 + c2)
"""


if __name__ == "__main__":

    #Constantes
    NF = 60

    #Entrada
    c1 = int(input("Ingrese nota certamen 1: "))
    c2 = int(input("Ingrese nota certamen 2: "))
    NL = int(input("Ingrese nota laboratorio: "))

    #Proceso
    NC = (NF - (NL *.3)) /.7
    c3 = NC*3 - (c1 + c2)

    #Salida
    print(f" Necesita nota {c3} en el certamen 3")
