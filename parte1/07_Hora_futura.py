"""
Hora futura:
    Escriba un programa que pregunte al usuario la hora actual t del reloj y un 
    número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

Ejemplos:
    Hora actual: 3
    Cantidad de horas: 5
    En 5 horas, el reloj marcara las 8

    Hora actual: 11
    Cantidad de horas: 43
    En 43 horas, el reloj marcara las 6

"""

if __name__ == "__main__":
    #Entrada
    hora_actual = int(input("Hora actual: "))
    cantidad_horas_a_sumar = int(input("Cantidad de horas: "))

    #Proceso
    cantidad_horas_a_sumar = cantidad_horas_a_sumar%12
    
    hora_futuro = hora_actual + cantidad_horas_a_sumar
    
    if hora_futuro > 12:
        hora_futuro = hora_futuro -12

    #Salida
    print(hora_futuro)