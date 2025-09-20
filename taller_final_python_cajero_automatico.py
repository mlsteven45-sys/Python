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

saldo = 10000  # Saldo inicial del cajero
historial = []  # Lista para guardar transacciones (tuplas con operaciones)

# === FUNCIÓN PARA PEDIR CLAVE ===
def pedir_clave(clave_correcta="1234", intentos_max=3) -> bool:
    """
    Pide la clave al usuario hasta intentos_max veces.
    Devuelve True si la clave es correcta, False si se agotan los intentos.
    """
    for intento in range(1, intentos_max + 1):
        clave = input(f"Ingrese su clave (intento {intento}/{intentos_max}): ").strip()
        if clave == clave_correcta:
            print("Clave correcta. Acceso concedido.\n")
            return True
        else:
            print("Clave incorrecta.")
    print("Se agotaron los intentos. Acceso denegado.")
    return False

# === FUNCIONES DEL CAJERO ===
def consultar_saldo():
    print(f"\nSu saldo actual es: {saldo}")
    historial.append(("Consulta", saldo))

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

def ver_historial():
    if not historial:
        print("\nNo hay transacciones registradas")
    else:
        print("\nHistorial de transacciones:")
        for i, transaccion in enumerate(historial, start=1):
            print(f"{i}. {transaccion}")

# === MENÚ PRINCIPAL ===
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

# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    if pedir_clave():  # Solo entra al menú si la clave es correcta
        menu()
