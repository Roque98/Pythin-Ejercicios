"""
Número invertido
    Escriba un programa que pida al usuario 
    un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

Ejemplos:
    Ingrese numero: 345
    543

    Ingrese numero: 241
    142

"""

if __name__ == "__main__":
    #entrada
    digitos = input("Ingrese numero: ")
    #proceso
    digitos = digitos[2] + digitos[1] + digitos[0]
    #salida
    print(digitos)