"""
Pitágoras
    Escriba un programa que reciba como entrada las longitudes
    de los dos catetos a y b de un triángulo rectángulo, y que 
    entregue como salida el largo de la hipotenusa c del triangulo,
    dado por el teorema de Pitágoras: c2=a2+b2.

Ejemplo:
    Ingrese cateto a: 7
    Ingrese cateto b: 5
    La hipotenusa es 8.6023252670426267


"""
import math


if __name__ == "__main__":
    #Entrada
    catetoA = float(input("Ingrese cateto a: "))
    catetoB = float(input("Ingrese cateto b: "))

    #Proceso
    hipotenusa = math.sqrt( catetoA**2 + catetoB**2)

    #Salida
    print(f'La hipotenusa es {hipotenusa}')