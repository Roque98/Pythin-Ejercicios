"""
Conversión de unidades de longitud
    Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

Ejemplo:
    Ingrese longitud: 45
    45 cm = 17.7165 in

    Ingrese longitud: 13
    13 cm = 5.1181 in

"""

if __name__ == "__main__":
    #Entrada
    centimetros = float(input("Ingrese longitud: "))

    #Proceso
    pulgadas = centimetros/2.54

    #Salida
    print(f"{centimetros} cm = {round(pulgadas, 4)} in")
