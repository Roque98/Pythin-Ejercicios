"""
Años bisiestos:
    Cuando la Tierra completa una órbita alrededor del Sol,
    no han transcurrido exactamente 365 rotaciones sobre sí misma, sino un poco más. 
    Más precisamente, la diferencia es de más o menos un cuarto de día.

    Para evitar que las estaciones se desfasen con el calendario, 
    el calendario juliano introdujo la regla de introducir un día adicional 
    en los años divisibles por 4 (llamados bisiestos), para tomar en 
    consideración los cuatro cuartos de día acumulados.

    Sin embargo, bajo esta regla sigue habiendo un desfase, 
    que es de aproximadamente 3/400 de día.

    Para corregir este desfase, en el año 1582 el papa Gregorio 
    XIII introdujo un nuevo calendario, en el que el último año 
    de cada siglo dejaba de ser bisiesto, a no ser que fuera 
    divisible por 400.

    Escriba un programa que indique si un año es bisiesto o no, 
    teniendo en cuenta cuál era el calendario vigente en ese año.

Ejemplos:

Ingrese un anno: 1988
1988 es bisiesto

Ingrese un anno: 2011
2011 no es bisiesto

Ingrese un anno: 1700
1700 no es bisiesto

Ingrese un anno: 1500
1500 es bisiesto

Ingrese un anno: 2400
2400 es bisiesto


"""


"""
ANALISIS:
    p : es divisible entre 4
    q : es el ultimo año del siglo
    r : es divisible entre 400
    s : El año es bisiesto

s <->  (p and ¬q)  or ( p and q and r )
"""
def divisible_entre_numero(anio, numero):
    return anio%numero==0
    


if __name__ == "__main__":

    # Entrada
    anio = int(input("Ingrese un año: "))

    # Proceso
    p = anio%4==0      # divisble entre 4 ?
    q = anio%100==0    # ultimo año siglo ?
    r = anio%400==0    # divisible entre 400?

    s = (p and not q)  or ( p and q and r )

    # Salida
    if(s):
        print(f"{anio} es bisiesto")
    else:
        print(f"{anio} no es bisiesto")