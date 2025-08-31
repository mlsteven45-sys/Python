#Suma de positivos y negativos

def contar_numeros (positivo, negativo, cero):
    for i in range (5):
        numero = int(input("Ingrese un numero entero: "))
        if numero > 0:
            print(f"el numero {numero} es positivo")
        elif numero < 0:
            print(f"el numero {numero} es negativo")
        else:
            print(f"el numero {numero} es igual a cero")

positivo = 0
negativo = 0
cero = 0
contar_numeros (positivo, negativo, cero)



# 2. Cuadrados perfectos
def cuadrados_perfectos(n):
    for i in range(1, n + 1):
        cuadrado = i ** 2
        if cuadrado %2 == 0:
            print(f"{i} - 2^ = {cuadrado} (par)")
        else:
            print(f"{i} - 2^ = {cuadrado}")

n = int(input("Ingrese un numero: "))
cuadrados_perfectos(n)




# 3. El usuario ingresa una palabra y una letra. El programa recorre la palabra y cuenta cuántas veces aparece esa letra. Si la letra no aparece, mostrar un mensaje indicándolo.
def contar_letra(palabra, letra):
    contador = 0
    for i in range(len(palabra)):
        if palabra[i] == letra:
            contador += 1
    return contador

palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")

resultado = contar_letra(palabra, letra)

if resultado == 0:
    print("La letra no aparece en la palabra.")
else:
    print(f"La letra aparece {resultado} veces.")



# 4. Números primos en un rango: El usuario ingresa un número límite y el programa imprime todos los números primos entre 1 y ese límite.
def es_primo (n):
    if n < 2:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

limite = int(input("Ingrese un numero limite: "))
print(f"Numeros primos entre 1 y {limite:}")
for i in range(1, limite + 1):
    if es_primo(i):
        print(i)

# 5.  Un profesor ingresa 5 notas (de 0 a 5). El programa debe mostrar cada nota y clasificarla como Aprobada o Reprobada. Al final, mostrar el total de aprobadas y reprobadas

def clasificar_notas ():
    aprobadas = 0
    reprobadas = 0
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i+1}:"))
        print(f"La nota ingrese fue: {nota}")
        if nota >= 3:
            print("Aprobada.")
            aprobadas += 1
    
        else:
             reprobadas < 3
             print("Reprobado")
             reprobadas += 1
        
    
    print(f"\nTotal de notas aprobadas: {aprobadas}")
    print(f"\Total de notas reprobadas: {reprobadas}")

clasificar_notas()