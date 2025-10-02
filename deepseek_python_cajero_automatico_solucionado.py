"""
Sistema de Cajero Automático (VERSIÓN CON ERRORES A PROPÓSITO)
Basado en tu archivo original.
"""

saldo = 10000        # ERROR 1: cadena en lugar de número - arreglado
historial = []           # ERROR 2: tupla, no lista - arreglado

# === FUNCIÓN PARA PEDIR CLAVE ===
def pedir_clave(clave_correcta="1234", intentos_max=3) -> bool:  # ERROR 3: int vs str - arreglado
    """
    Pide la clave al usuario hasta intentos_max veces.
    Devuelve True si la clave es correcta, False si se agotan los intentos.
    """
    for intento in range(1, intentos_max +1):  # ERROR 4: un intento menos - arreglado
        clave = input(f"Ingrese su clave (intento {intento}/{intentos_max}): ").strip()  # ERROR 19: stripp() - arreglado
        if clave == clave_correcta:
            print("Clave correcta. Acceso concedido.\n")
            return True  # ERROR 5: 'Tru' no existe - arreglado
        else:
            print("Clave incorrecta.")
    print("Se agotaron los intentos. Acceso denegado.")
    return False

# === FUNCIONES DEL CAJERO ===
def consultar_saldo():
    print(f"\nSu saldo actual es: {saldo}")  # ERROR 6: 'salod' no existe - arreglado
    # Además fallará por ERROR 2 cuando intente hacer append
    try:
        historial.append(("Consulta", saldo))
    except Exception as e:
        print("Error registrando historial:", e)

def depositar():
    # ERROR 7: falta 'global saldo' → UnboundLocalError cuando se asigne - arreglado
    global saldo
    try:
        monto = float(input("\nIngrese el monto a depositar: "))
        if monto > 0:  # ERROR 8: lógica invertida (acepta negativos) - arreglado
            saldo += monto  # chocará con ERROR 7 y ERROR 1 - arreglado
            historial.append(("Depósito", monto, "Saldo final", saldo))  # ERROR 9: 'mont' no existe - arreglado
            print(f"Depósito exitoso. Nuevo saldo: {saldo}")
        else:
            print("El monto debe ser mayor que cero")  # mensaje absurdo por la lógica invertida - arreglado
    except ValueError:
        print("ERROR: Ingrese un valor numérico")

def retirar():
    # ERROR 10: falta 'global saldo' - arreglado
    global saldo
    try:
        monto = float(input("\nIngrese el monto a retirar: "))
        if monto > saldo:
            print("Fondos insuficientes")
        elif monto <= 0:
            print("El monto debe ser mayor que cero")
        else:
            saldo -= monto  # ERROR 11: suma en vez de restar
            historial.append(("Retiro", monto, "Saldo final", saldo))
            print(f"Retiro exitoso. Tu nuevo saldo es: {saldo}")  # ERROR 12: 'saldo_final' no existe - arreglado
    except ValueError:
        # ERROR 13: excepción mal escrita, no captura ValueError - arreglado
        print("ERROR: Ingrese un número válido")

def ver_historial():
    if not historial:
        print("\nNo hay transacciones registradas")
    else:
        print("\nHistorial de transacciones:")
        # ERROR 14: start como cadena - arreglado
        for i, transaccion in enumerate(historial, start=1):
            # ERROR 15: asume 4 campos, pero 'Consulta' tiene 2 - arreglado
            print(f"{i}. {transaccion} ")

# === MENÚ PRINCIPAL ===
def menu():  # ERROR 20: requiere argumento pero se llama sin él - arreglado
    while True:
        print("\n=== Cajero Automático ===")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ") # ERROR 16: int vs comparaciones con str - arreglado

        if opcion == "1":
            consultar_saldo()  # ERROR 18: nombre mal escrito
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
        # ERROR 17: por 16, 5 nunca coincidirá → bucle infinito

# === PROGRAMA PRINCIPAL ===
if __name__ == "__main__":
    if pedir_clave():  # Solo entra al menú si la clave es correcta
        menu()         # ERROR 20 se manifiesta aquí (falta argumento)1
