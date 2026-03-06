# Este código es un sistema para realizar recargas de la tarjeta del Metro, MetroBus y Terminal de Buses.

# Imprime encabezados informativos del sistema
print("\n-----------------------------------------------------------------------")
print("---\nRecarga de Tarjeta para Metro / MetroBus / Terminal de Buses---")
print("\nEL Equipo solo Acepta Monedas $ (Martinelis) y Billetes $ (No da Vuelto)")
print("\n-----------------------------------------------------------------------")

# Saldo inicial de la tarjeta
saldo = 2.75  # La tarjeta comienza con $2.75

# Función para pedir un monto válido al usuario
def pedir_monto(mensaje):
    while True:
        monto = input(mensaje).strip()  # Pide el monto y elimina espacios al inicio y fin

        # Verifica si se ingresó algún valor
        if monto == "":
            print("ERROR: Debe ingresar un monto.")
            continue  # Vuelve a pedir el monto

        # Verifica que el valor ingresado sea un número (puede tener un punto decimal)
        if not monto.replace(".", "", 1).isdigit():
            print("ERROR: Solo se permiten números.")
            continue

        monto_float = float(monto)  # Convierte el monto a tipo float
        if monto_float <= 0:  # El monto debe ser mayor que 0
            print("ERROR: El monto debe ser mayor que 0.")
            continue

        return monto_float  # Si todo está correcto, devuelve el monto como float

# Verificación de que la tarjeta fue insertada
while True:
    tarj = input("¿Ha ingresado su tarjeta? (si/no): ").lower().strip()  # Normaliza a minúsculas y elimina espacios

    if tarj == "si":
        print("--- Tarjeta Reconocida Exitosamente ---")
        break  # Sale del bucle si la tarjeta fue reconocida
    elif tarj == "no":
        print("--- Inserte la tarjeta para continuar ---")  # Pide insertar la tarjeta
    else:
        print("Opción no válida. Por favor, escriba 'si' o 'no'.")  # Si no es "si" o "no"

# Menú principal del sistema
while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Recarga en Monedas")
    print("2. Recarga en Billetes")
    print("3. Consulta de Saldo")
    print("4. Activación de Recarga Electrónica")
    print("5. Salir")
    print("----------------------------------------------------------------")

    # Pide al usuario seleccionar una opción del menú
    opcion = input("\nSelecciona una opción: ").strip()

    if opcion == "1":
        # Recarga usando monedas
        monto = pedir_monto("Ingrese el monto en monedas que desea recargar: $")
        saldo += monto  # Se suma el monto ingresado al saldo actual
        print(f"Su recarga ha sido EXITOSA, su nuevo saldo es de: ${saldo:.2f}")
        print("---\nPOR FAVOR RETIRE SU TARJETA, GRACIAS ---")
        
    elif opcion == "2":
        # Recarga usando billetes
        monto = pedir_monto("Ingrese el monto en billetes que desea recargar: $")
        saldo += monto
        print(f"Su recarga ha sido EXITOSA, su nuevo saldo es de: ${saldo:.2f}")
        print("---\nPOR FAVOR RETIRE SU TARJETA, GRACIAS ---")

    elif opcion == "3":
        # Consulta del saldo actual
        print(f"Su saldo actual es de: ${saldo:.2f}")
        print("---\nPOR FAVOR RETIRE SU TARJETA, GRACIAS ---")

    elif opcion == "4":
        # Recarga electrónica (por transferencia u otro método)
        monto = pedir_monto("Ingrese el monto de la recarga electrónica para validar en el sistema: $")
        saldo += monto
        print("Recarga por transferencia exitosa.")
        print(f"\nSu nuevo saldo es: ${saldo:.2f}")

    elif opcion == "5":
        # Salir del sistema
        print("S\naliendo del Sistema de Recarga...")
        break  # Termina el bucle y finaliza el programa

    else:
        # Opción inválida
        print("\nOpción no válida, intenta de nuevo.")