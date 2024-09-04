""""
Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un 
total de numeros de personas
"""
# Solicitar el total de personas en el salón
totalPersonas = int(input("Ingresa el total de personas en el salón de clases: "))

# Solicitar el número de hombres en el salón
numeroHombres = int(input("Ingresa el número de hombres en el salón de clases: "))

# Calcular el número de mujeres
numeroMujeres = totalPersonas - numeroHombres

# Mostrar el resultado
print(f"Cantidad de hombres: {numeroHombres}")
print(f"Cantidad de mujeres: {numeroMujeres}")

