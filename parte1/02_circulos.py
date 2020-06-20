"""
Círculos
    Escriba un programa que reciba como entrada el radio de un círculo
    y entregue como salida su perímetro y su área:

Ejemplo: 
    Ingrese el radio: 5
    Perimetro: 31.4
    Área: 78.5

"""

import math

def getArea(radio):
    return math.pi * radio**2

def getPerimetro(radio):
    return 2 * math.pi * radio

if __name__ == "__main__":
    # Entrada
    radio = float(input("Ingrese el radio: "))

    # Proceso
    perimetro = round(getPerimetro(radio), 2)
    area = round(getArea(radio), 2)

    # Salida
    print(f'Perimetro: {perimetro}')
    print(f'Área: {area}')