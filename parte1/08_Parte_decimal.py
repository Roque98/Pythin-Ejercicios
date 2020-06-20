"""
Parte decimal
    Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

Ejemplo:
    Ingrese un numero: 4.5
    0.5

    Ingrese un numero: -1.19
    0.19
"""
import math

if __name__ == "__main__":
    # Entrada
    numero_entrada = float(input("Ingrese un numero: "))
    # Proceso
    parte_decimal, parte_entera = math.modf(numero_entrada)
    # Salida
    print(abs(round(parte_decimal,5)))
