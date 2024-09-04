""""
Una persona debe realizar un muestreo con 50 personas para determinar el 
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. 
Las categorías se determinar de acuerdo a la siguiente tabla:

CATEGORIA          EDAD
Niños              0 - 12 
Jovenes            13 - 29
Adultos            30 - 59
Ancianos           60 en adentante
"""
# Iniciar los acumuladores de peso y contadores para cada categoría
sumaPesoNiños = 0
contadorNiños = 0

sumaPesoJovenes = 0
contadorJovenes = 0

sumaPesoAdultos = 0
contadorAdultos = 0

sumaPesoAncianos = 0
contadorAncianos = 0

# Realizar el muestreo para 50 personas
for i in range(5):
    edad = int(input("Ingrese la edad de la persona: "))
    peso = float(input("Ingrese el peso de la persona en kg: "))
    
    # Clasificar según la edad
    if 0 <= edad <= 12:
        sumaPesoNiños += peso
        contadorNiños += 1
    elif 13 <= edad <= 29:
        sumaPesoJovenes += peso
        contadorJovenes += 1
    elif 30 <= edad <= 59:
        sumaPesoAdultos += peso
        contadorAdultos += 1
    elif edad >= 60:
        sumaPesoAncianos += peso
        contadorAncianos += 1

# Calcular y mostrar los promedios de peso
if contadorNiños > 0:
    print(f"Promedio de peso de niños: {sumaPesoNiños / contadorNiños:.2f} kg")
if contadorJovenes > 0:
    print(f"Promedio de peso de jóvenes: {sumaPesoJovenes / contadorJovenes:.2f} kg")
if contadorAdultos > 0:
    print(f"Promedio de peso de adultos: {sumaPesoAdultos / contadorAdultos:.2f} kg")
if contadorAncianos > 0:
    print(f"Promedio de peso de ancianos: {sumaPesoAncianos / contadorAncianos:.2f} kg")
