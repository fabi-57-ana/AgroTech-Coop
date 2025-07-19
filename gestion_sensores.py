
def registrar_tipo_sensor():
    print("\nFunciÃ³n registrar_tipo_sensor() invocada")

def registrar_sensor_instalado():
    print("\nFunciÃ³n registrar_sensor_instalado() invocada")

def menu_sensores():
    print("\n=== GESTIÃ“N DE SENSORES ===")
    print("1. Registrar tipo de sensor")
    print("2. Registrar sensor instalado")
    print("3. Volver al menÃº principal")
    
    opcion = input("Seleccione una opciÃ³n: ")
    
    if opcion == "1":
        registrar_tipo_sensor()
    elif opcion == "2":
        registrar_sensor_instalado()
    elif opcion == "3":
        return
    else:
        print("OpciÃ³n no vÃ¡lida")
