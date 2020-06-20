"""
Determinar par
    Escriba un programa que determine si el número entero
    ingresado por el usuario es par o no.

Ejemplo:
    Ingrese un número: 4
    Su número es par

    Ingrese un número: 3
    Su número es impar  

"""

if __name__ == "__main__":

    # Entrada
    numero = int(input("Ingrese un número: "))


    # Proceso Y SALIDA
    if numero %2 == 0:
        print("Su número es par")
    else:
        print("Su número es impar")