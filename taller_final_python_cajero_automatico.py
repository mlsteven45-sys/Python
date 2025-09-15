"""
Sistema de Cajero Automático
Autor: [Tu Nombre]
Descripción:
    Programa que simula un cajero automático con las siguientes opciones:
    - Consultar saldo
    - Depositar dinero
    - Retirar dinero
    - Ver historial de transacciones
    - Salir
Cada transacción se guarda como una tupla dentro de una lista.
"""

saldo = 10000 # Saldo inicial del cajero
historial = [] # lista para guardar transacciones (En esta lista se guardan las tuplas)

def consultar_saldo():
    #esta funcion muestra el saldo y lo guarda en el historial en lista []
    print(f"\nSu saldo actual es: {saldo}") # imprimir
    historial.append(("Consulta", saldo)) # Tupla y diccionario

def depositar():
    global saldo
    try:
        monto = float(input("\nIngrese el monto a depositar: "))
        if monto > 0:
            saldo += monto
            historial.append(("Deposito realizado: ", monto, "Saldo final: ", saldo))
            print(f"Deposito exitoso. Nuevo saldo: {saldo}")
        else:
            print("El monto debe ser mayor a cero")
    except ValueError:
        print("ERROR: Ingrese un valor numerico")

def retirar():
    global saldo
    try:
        monto = float(input("\nIngrese el monto a Retirar: "))
        if monto > saldo:
            print("Fondos insuficientes")
        elif monto <= 0:
            print("El monto debe ser mayor que cero")
        else:
            saldo -= monto
            historial.append(("Retiro realizado", monto, "Saldo final: ", saldo))
            print(F"Retiro exitoso. Tu nuevo saldo es: {saldo}")
    except ValueError:
        print("ERROR: ingrese un numero valido")

def ver_historial():
    if not historial:
        print("\nNo hay transacciones registradas")
    else:
        print("\nHistorial de transacciones.")
        for i, transaccion in enumerate(historial, start=1):
            print(f"{i}. {transaccion}")

def menu():
    while True:
        print("\n=== Cajero Automatico ===")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            print("Gracias por usar el cajero automatico. ¡Hasta pronto!")
            break
        else:
            print("Opcion invalida. Intente de nuevo")

if __name__ == "__main__":
    menu()

