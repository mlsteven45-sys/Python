# Python
...DOCUMENTACION DE UN EJERCICIO DE PYTHON 
            (CAJERO AUTOMATICO)...

Por: Stiven Mejía y Juan Camilo Vargas Resstrepo

                Fecha: 18/sep/2025

                Programa: ADSO

                ...introducción...
 
Este programa simula un cajero automático. permite al usuario entrar con las clave, consultar saldo, depositar dinero, retirar dinero, ver el historial de las transacciones, y salir.

este programa contiene funciones, ciclos, condicionales, diccionarios y tuplas los cuales permiten hacer la función 

                ...Objetivo del programa...

* Objetivo general: 
Desarrollar un programa que simule las operaciones basicas de un cajeroa automatico.
* Objetivo específicos:
1. Practicar el uso de condicionales (if, elif, else, try, except)
2. Utilizar ciclos (for y while) para mantener el programa activo hasta que el usuario decida salir.
3. Trabajar con funciones para tener el programa organizado.
4. manejar datos de entrada (input) y salida (print)

                    ...Requerimiento...

* Lenguaje: Python 3.12
* Editor: Visual Studio Code
* Conocimientos Previos:
    - Funciones
    - Ciclos
    - Condicionales
    - Variables
    - Listas
    - Tuplas
    - Manejo de errores básicos

                    ...Diseño del programa...

Sistema de Cajero Automático
    Descripción:
        Programa que simula un cajero automático con las siguientes opciones:
        - Ingresar Clave
        - Consultar saldo
        - Depositar saldo
        - Retirar saldo
        - Ver hostorial de transacciones
        - Salir
    Leer opción
    Ejecutar la operación seleccionada
    Volver al menú hasta que se elija salir
    Fin

                    ... Explicacion del código...

Definicion de las variables:
    - Saldo: se define con un numero tipo float (Numero decimal).
    - historial: se convierte en lista, para guardar los datos que el usuario ingresa y se imprime el resultado en la lista con el metodo (append)
    - intento e intento_max: estas variable estan definidas para un limite de intentos para ingresar la clave.
    - monto: esta variable esta definida en la funcion depositar y retirar

                    ...Funciones creadas...

def pedir_clave(clave_correcta="1234", intentos_max=3) -> bool:
    for intento in range(1, intentos_max + 1):
        clave = input(f"Ingrese su clave (intento {intento}/{intentos_max}): ").strip()
        if clave == clave_correcta:
            print("Clave correcta. Acceso concedido.\n")
            return True
        else:
            print("Clave incorrecta.")
    print("Se agotaron los intentos. Acceso denegado.")
    return False

    """Esta funcion es para pedir la clave del usuario para depositar y  retirar"""
    """
    Pide la clave al usuario hasta intentos_max veces.
    Devuelve True si la clave es correcta, False si se agotan los intentos.
    """

def consultar_saldo():
    print(f"\nSu saldo actual es: {saldo}")
    historial.append(("Consulta", saldo))

    """Esta funcion muestra el saldo actual del usuario"""

def depositar():
    global saldo
    try:
        monto = float(input("\nIngrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            historial.append(("Depósito", monto, "Saldo final", saldo))
            print(f"Depósito exitoso. Nuevo saldo: {saldo}")
        else:
            print("El monto debe ser mayor a cero")
    except ValueError:
        print("ERROR: Ingrese un valor numérico")

    """"esta funcion permite que el usuario pueda depositar su dinero"""

def retirar():
    global saldo
    try:
        monto = float(input("\nIngrese el monto a retirar: "))
        if monto > saldo:
            print("Fondos insuficientes")
        elif monto <= 0:
            print("El monto debe ser mayor que cero")
        else:
            saldo -= monto
            historial.append(("Retiro", monto, "Saldo final", saldo))
            print(f"Retiro exitoso. Tu nuevo saldo es: {saldo}")
    except ValueError:
        print("ERROR: Ingrese un número válido")

    """Esta funcion permite que el usuario pueda retirar del cajero"""

def ver_historial():
    if not historial:
        print("\nNo hay transacciones registradas")
    else:
        print("\nHistorial de transacciones:")
        for i, transaccion in enumerate(historial, start=1):
            print(f"{i}. {transaccion}")

    """Esta funcion permite que el usuario pueda ver todos sus movimientos en el cajero automatico"""

def menu():
    while True:
        print("\n=== Cajero Automático ===")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            print("Gracias por usar el cajero automático. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo")

    """Esta funcion es la que permite que el usuario escoja la opcion que necesita despues de ingresar la clave y pueda gestionar su necesidad en cada opcion."""

                ...Ejemplo de ejecución...

1. El programa pide una clave al usuario:
        Ingrese su clave (intento 1/3): 1234
        Clave correcta. Acceso concedido.


        === Cajero Automático ===        
        1. Consultar Saldo
        2. Depositar
        3. Retirar
        4. Ver historial
        5. Salir
        Seleccione una opción: 

2. Seleccionamos la opcion consiltar saldo:
        === Cajero Automático ===        
        1. Consultar Saldo
        2. Depositar
        3. Retirar
        4. Ver historial
        5. Salir
        Seleccione una opción: 1

        Su saldo actual es: 10000

3. Seleccionamos la opcion Depositar:
        === Cajero Automático ===
        1. Consultar Saldo
        2. Depositar
        3. Retirar
        4. Ver historial
        5. Salir
        Seleccione una opción: 2

        Ingrese el monto a depositar: 40000
        Depósito exitoso. Nuevo saldo: 50000.0

4. Seleccionamos la opcion retirar:
        === Cajero Automático ===
        1. Consultar Saldo
        2. Depositar
        3. Retirar
        4. Ver historial
        5. Salir
        Seleccione una opción: 3

        Ingrese el monto a retirar: 30000
        Retiro exitoso. Tu nuevo saldo es: 20000.0

5. Seleccionamos la opciom Ver historial:
        === Cajero Automático ===
        1. Consultar Saldo
        2. Depositar
        3. Retirar
        4. Ver historial
        5. Salir
        Seleccione una opción: 4

        Historial de transacciones:
        1. ('Consulta', 10000)
        2. ('Depósito', 40000.0, 'Saldo final', 50000.0)
        3. ('Retiro', 30000.0, 'Saldo final', 20000.0)

6. la opcion Salir te saca del cajero y ya no funcionaria mas, esta opcion la pone el usuario cuando ya no quiere seguir o termina con una transaccion.

            ...Conclusión...

El cajero permite simular un cajero basico.
fue util para practicar estructuras de control y funciones.