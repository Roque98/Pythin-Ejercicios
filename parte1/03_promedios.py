"""
Promedios:
    Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario
Ejemplo:
    Primera nota: 55
    Segunda nota: 71
    Tercera nota: 46
    Cuarta nota: 87
    El promedio es: 64.75
"""

if __name__ == "__main__":
    #Entrada
    nota1 = float(input("Primera nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Tercera nota: "))
    nota4 = float(input("Cuarta nota: "))

    #Proceso
    promedio = (nota1 + nota2 + nota3 + nota4)/4

    #Salida
    print(f"El promedio es: {promedio}")