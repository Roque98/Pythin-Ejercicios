"""
Palabra más larga
    Escriba un programa que pida al usuario dos palabras, y que indique cuál 
    de ellas es la más larga y por cuántas letras lo es.

Ejemplos.
    Palabra 1: edificio
    Palabra 2: tren
    La palabra edificio tiene 4 letras mas que tren.

    Palabra 1: sol
    Palabra 2: paralelepipedo
    La palabra paralelepipedo tiene 11 letras mas que sol
"""

if __name__ == "__main__":
    #Entrada 
    palabra_1 = input("Palabra 1: ")
    palabra_2 = input("Palabra 2: ")

    diferencia_longitud = abs(len(palabra_1) - len(palabra_2))

    #Proceso
    if len(palabra_1) > len(palabra_2):
        print(f"La palabra {palabra_1} tiene {diferencia_longitud} letras mas que {palabra_2}")
    else:
        print(f"La palabra {palabra_2} tiene {diferencia_longitud} letras mas que {palabra_1}")