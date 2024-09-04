""""
Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa 
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio 
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos 
que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad 
sea igual a 0
"""
# Inicializamos las variables necesarias
cantidadHombres = 0  # Para contar la cantidad de hombres
cantidadMujeres = 0  # Para contar la cantidad de mujeres
sumaAlturas = 0.0  # Para acumular las alturas de todos los alumnos
cantidadAlumnos = 0  # Para contar el número total de alumnos
alturaMayor170 = 0  # Para contar alumnos con altura mayor a 1.70 m
alturaMenorIgual150 = 0  # Para contar alumnos con altura menor o igual a 1.50 m

# Iniciamos un bucle para pedir los datos de los alumnos
while True:
    # Pedimos la edad del alumno
    edad = int(input("Ingrese la edad del alumno (0 para finalizar): "))
    
    # Si la edad es 0, finalizamos el bucle
    if edad == 0:
        break
    
    # Pedimos el sexo del alumno
    sexo = input("Ingrese el sexo del alumno (M para hombre, F para mujer): ")
    
    # Pedimos la altura del alumno
    altura = float(input("Ingrese la altura del alumno en metros (por ejemplo, 1.75): "))
    
    # Aumentamos el contador de alumnos
    cantidadAlumnos += 1
    
    # Sumamos la altura a la acumulación total de alturas
    sumaAlturas += altura
    
    # Contamos la cantidad de hombres y mujeres según el sexo
    if sexo == 'M':
        cantidadHombres += 1
    elif sexo == 'F':
        cantidadMujeres += 1
    
    # Contamos cuántos alumnos tienen una altura mayor a 1.70 m
    if altura > 1.70:
        alturaMayor170 += 1
    
    # Contamos cuántos alumnos tienen una altura menor o igual a 1.50 m
    if altura <= 1.50:
        alturaMenorIgual150 += 1

# Calculamos la altura promedio del grupo
if cantidadAlumnos > 0:
    alturaPromedio = sumaAlturas / cantidadAlumnos
else:
    alturaPromedio = 0  # Si no hay alumnos, el promedio es 0

# Mostramos los resultados finales
print("Cantidad de hombres:", cantidadHombres)
print("Cantidad de mujeres:", cantidadMujeres)
print("Altura promedio del grupo:", alturaPromedio)
print("Cantidad de alumnos con altura mayor a 1.70 m:", alturaMayor170)
print("Cantidad de alumnos con altura menor o igual a 1.50 m:", alturaMenorIgual150)
