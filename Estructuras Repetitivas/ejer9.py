""""
Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos
"""
# Inicializamos las variables para acumular las edades y contar el número de hombres y mujeres
edadHombresTotal = 0
edadMujeresTotal = 0
cantidadHombres = 0
cantidadMujeres = 0

# Definimos el número total de alumnos que vamos a procesar
totalAlumnos = 5  # Puedes cambiar este valor según el número de alumnos

# Iniciamos un ciclo for para procesar los datos de cada alumno
for i in range(totalAlumnos):
    # Solicitamos la edad del alumno
    edad = int(input("Ingrese la edad del alumno: "))
    
    # Solicitamos el género del alumno
    genero = input("Ingrese el género del alumno (M para hombre, F para mujer): ")
    
    # Si el género es masculino, sumamos la edad a la acumulación de hombres y aumentamos el contador de hombres
    if genero == 'M':
        edadHombresTotal += edad
        cantidadHombres += 1
    
    # Si el género es femenino, sumamos la edad a la acumulación de mujeres y aumentamos el contador de mujeres
    elif genero == 'F':
        edadMujeresTotal += edad
        cantidadMujeres += 1

# Calculamos el promedio de edades para los hombres si hay al menos un hombre
if cantidadHombres > 0:
    promedioHombres = edadHombresTotal / cantidadHombres
else:
    promedioHombres = 0  # Si no hay hombres, el promedio es 0

# Calculamos el promedio de edades para las mujeres si hay al menos una mujer
if cantidadMujeres > 0:
    promedioMujeres = edadMujeresTotal / cantidadMujeres
else:
    promedioMujeres = 0  # Si no hay mujeres, el promedio es 0

# Calculamos el promedio total del grupo, considerando a todos los alumnos
promedioTotal = (edadHombresTotal + edadMujeresTotal) / (cantidadHombres + cantidadMujeres)

# Imprimimos los resultados
print("Promedio de edad de los hombres:", promedioHombres)
print("Promedio de edad de las mujeres:", promedioMujeres)
print("Promedio de edad total del grupo:", promedioTotal)
