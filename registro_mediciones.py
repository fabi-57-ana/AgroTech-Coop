
def registrar_medicion():
    print("\nFunción registrar_medicion() invocada")

def menu_mediciones():
    print("\n=== REGISTRO DE MEDICIONES ===")
    print("1. Registrar medición")
    print("2. Volver al menú principal")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_medicion()
    elif opcion == "2":
        return
    else:
        print("Opción no válida")