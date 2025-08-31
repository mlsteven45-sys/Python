# 1.	Escribe un programa que pida un número entero y muestre su tabla de multiplicar del 1 al 10.

numero = int(input("Ingresar un numero entero: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)


# 2. Programa que calcula la suma de numeros entre 1 y n

n = int(input("Ingresa un numero entero positivo: "))
suma = 0
for i in range(1, n+1):
    if i % 2 == 0:
        suma += i
print(f"La suma de los numeros pares entre 1 y {n} es: {suma}")

# 3. Programa con menu de operaciones matematicas

while True:
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = int(input("Elige una opción (1-5): "))

    if opcion == 5:
        print("Saliendo del programa... ")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print(f"La suma es: {num1 + num2}")
    elif opcion == 2:
        print(f"La resta es: {num1 - num2}")
    elif opcion == 3:
        print(f"La multiplicación es: {num1 * num2}")
    elif opcion == 4:
        if num2 != 0:
            print(f"La división es: {num1 / num2}")
        else:
            print("Error: no se puede dividir entre 0 ")
    else:
        print("Opción no válida, intenta de nuevo.")




# 4. Escribe un programa que pida un año y determine si es bisiesto o no
anio = int(input("Ingresa un año: "))
if (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} NO es bisiesto")