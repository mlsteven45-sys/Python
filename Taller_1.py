# 1. Area de un cuadrado
lado = float(input("ingrese el lado del cuadrado: "))
if lado < 0:
    print("Error: el lado no puede ser negativo.")
else: 
    area = lado * lado
    print(f"area del cuadrado = {area}")


# 2. Area de un circulo
import math
radio = float(input("ingrese el radio de un circulo:  "))
if radio < 0:
    print("Error: el radio no puede ser negativo.")
else:
    area = math.pi * (radio ** 2)
    print(f"Area del circulo = {area}")


# 3. Aporte de salud
salario = float(input("Ingrese salario: "))
aporte = salario * 0.04
print(f"Aporte a salud (4%) = {aporte}")






# 4. Volumen del cono
import math
radio = float(input("Ingrese el radio del cono: "))
altura = float(input("Ingrese altura del cono: "))
if radio < 0 or altura < 0:
    print("Error: ni el radio ni la altura pueden ser negativos: ")
else:
    volumen = (1/3) * math.pi * (radio ** 2) * altura
    print(f"El volumen del cono es: {volumen}")

# 5. Área de un triángulo: (base * altura) / 2 
base = float(input("Ingrese la base del triángulo: "))
altura = float(input ("Ingrese la altura del triángulo: "))
if base < 0 or altura < 0:
    print("Error: base y altura deben ser no negativas.")
else:
   area = (base * altura) / 2.0
   print(f"Área del triángulo = (area)")


# 6. Angulo, seno, coseno y tangente
angulo = float(input("Ingrese un angulo en grados: "))
radianes = math.radians(angulo)
print("Seno:", math.sin(radianes))
print("Coseno", math.cos(radianes))
print("Tangente", math.tan(radianes))




# 7. Nombre y pasarlo a minusculas
nombre = input("Ingrese un nombre: ")
print("En minusculas: ", nombre.lower())







# 8. Apellido y pasarlo a mayusculas
apellido = input("Ingrese un apellido: ")
print("En MAYUSCULAS: ", apellido.upper())







# 9. Capturar nombre completo y capitalizarlo
nombre_completo = input("Ingrese su nombre completo: ")
print("Capitalizado: ", nombre_completo.title())







# 10. ingrese de una frase y luego cuente la cantidad de 'a' que hay
frase = input("Ingrese una frase: ")
contador = 0
for letra in frase:
    if letra.lower() == "a":
        contador += 1
print("Cantidad de 'a' que hay:", contador)



# 11. Solicite el ingreso de una palabra y una letra, luego diga en qué posición está la letra que usted indicó.
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una palabra: ")
posicion = -1
for i in range(len(palabra)):
    if palabra [i].lower() == letra.lower():
        posicion = i + 1 
        break
if posicion != + -1:
    print("La letra esta en la posicion: ", posicion)
else:
    print("La letra no esta en la palabra. ")



# 12. •	13Cuente la cantidad de espacios en blanco hay en la siguiente frase: "Los campistas necesitan practicar mucho con python!, por eso, harán bastantes ejercicios!".
frase_fija = "Los campistas necesitan practicar mucho con python!, por eso, harán bastantes ejercicios!"
espacios = 0
for caracter in frase_fija:
    if caracter == " ":
        espacios += 1
print("Cantidad de espacios:", espacios)



#13. Divida la frase del ejercicio anterior en palabras.
palabras = frase_fija.split()
print("Palabras: ", palabras)


#14. Divida la frase anterior, por cada coma que encuentre.
partes = frase_fija.split(",")
print("Partes separados por comas: ", partes)


#15. Capture la edad de una persona y determine si es mayor de edad en Colombia.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad en Colombia")
else:
    print("Es menor de edad en Colombia")




#16. Capture la edad de una persona y determine si es mayor o menor de edad.
edad2 = int(input("Ingrese su edad: "))
if edad2 >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

#17. Capture el nombre de una persona y determine si es Bon Jovi Ernesto.
nombre2 = input("Ingrese un nombre: ")
if nombre2.lower() == "bon jovi ernesto":
    print("Si es Bon Jovi Ernesto")
else:
    print("No es Bon Jovi Ernesto")


#18. Capture dos números y determine cuál de ellos es el mayor, cual el menor o si son iguales.
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 > num2:
    print("El mayor es: ", num1)
    print("el menor es:", num2)
elif num2 > num1:
    print("El mayor es:", num2)
    print("El menor es:", num1)
else:
    print("Son iguales")



#19. Capture el sexo de una persona y salude a dicha de persona de manera adecuada según su sexo.
sexo = input("Ingrese su sexo (M/F): ")
if sexo.upper() == "M":
    print("¡Bienvenido!")
elif sexo.upper() == "F":
    print("¡Bienvenida!")
else:
    print("¡Bienvenid@!")


#20. Capture el salario de una persona y determine si dicho salario es integral.
salario = float(input("Ingrese el salario de la persona: "))
salario_minimo = 1300000
if salario >= 13 * salario_minimo:
    print("El salario es integral.")
else:
    print("El salario NO es integral.")



#21. Capture el peso y la altura de una persona, calcule el IMC y determine si dicha persona está en sobrepeso, peso normal o desnutrición.
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:2f}")

if imc < 18.5:
    print("Esta en desnutricion: ")
elif imc < 25:
    print("Esta en peso normal: ")
else:
    print("Esta en obesidad: ")


#22. Capture tres números y determine cuál de ellos es el mayor, cual el menor y cuál es el del medio.
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el primer numero: "))
c = int(input("Ingrese el primer numero: "))

numeros = [a, b, c]
numeros.sort()

print(f"El menor es: {numeros[0]}")
print(f"El del medio es: {numeros[1]}")
print(f"El mayor es: {numeros[2]}")