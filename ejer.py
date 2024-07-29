mensaje="hola, estoy aprendiendo python"
nombre="luisa"
formacion="adso"
edad="19"
estatura="1.65"
peso="55"
print(mensaje, "mi nombre es:" ,nombre, "soy de la formacion:" ,formacion, "tengo:" ,edad, "años" , 
"mido:" ,estatura, "y peso:" ,peso, "kg")  

#forma de imprimir 2
print(f"{mensaje}. mi nombre es: {nombre}, soy de la formacion: {formacion}, tengo: {edad}, años, mido: {estatura}, y peso: {peso} kg")

#ejercicio 2
n1 = 12
n2 = 4
suma= n1+ n2
print("la suma de: ",n1, "y",n2, "es: ",suma)
print(f"la suma de {n1} y {n2} es {suma}")
#resta
n1 = 12
n2 = 4
resta= n1- n2
print("la resta de: ",n1, "y",n2, "es: ",resta)
print(f"la resta de {n1} y {n2} es {resta}")
#multipicacion
n1 = 12
n2 = 4
multiplicacion= n1* n2
print("la multiplicacion de: ",n1, "y",n2, "es: ",multiplicacion)
print(f"la multiplicacion de {n1} y {n2} es {multiplicacion}")
#division cociente
n1 = 12
n2 = 4
divisioncociente= n1// n2
print("la division de: ",n1, "y",n2, "es: ",divisioncociente)
print(f"la division de {n1} y {n2} es {divisioncociente}")
#division residuo
n1 = 12
n2 = 4
divisionresiduo= n1% n2
print("la division de: ",n1, "y",n2, "es: ",divisionresiduo)
print(f"la division de {n1} y {n2} es {divisionresiduo}")

#ejercicio 3 pidiendo datos

n1=int(input("Digite un valor:  "))
n2=int(input("Digite otro valor: " ))
print(f"