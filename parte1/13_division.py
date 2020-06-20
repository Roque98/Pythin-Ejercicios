"""
División
    Escriba un programa que pida dos números enteros 
    y que calcule la división, indicando si la división es exacta o no.

Ejemplos:
    Dividendo: 14
    Divisor: 5

    La división no es exacta.
    Cociente: 2
    Resto: 4



    Dividendo: 100
    Divisor: 10

    La división es exacta.
    Cociente: 10
    Resto: 0
"""

if __name__ == "__main__":
    # Entrada
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))

    resto = dividendo%divisor
    # proceso 
    if resto == 0:
        print("La división es exacta")
        cociente = dividendo / divisor
    else:
        print("La división no es exacta")
        cociente = (dividendo-resto) / divisor

    # Salida
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")