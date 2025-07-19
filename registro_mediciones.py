
def registrar_medicion():
    print("\nFunciÃ³n registrar_medicion() invocada")

def menu_mediciones():
    print("\n=== REGISTRO DE MEDICIONES ===")
    print("1. Registrar mediciÃ³n")
    print("2. Volver al menÃº principal")
    
    opcion = input("Seleccione una opciÃ³n: ")
    
    if opcion == "1":
        registrar_medicion()
    elif opcion == "2":
        return
    else:
        print("OpciÃ³n no vÃ¡lida")
