def registrar_tipo_sensor():
    print("\nFunción registrar_tipo_sensor() invocada")

def registrar_sensor_instalado():
    print("\nFunción registrar_sensor_instalado() invocada")

def menu_sensores():
    print("\n=== GESTIÓN DE SENSORES ===")
    print("1. Registrar tipo de sensor")
    print("2. Registrar sensor instalado")
    print("3. Volver al menú principal")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_tipo_sensor()
    elif opcion == "2":
        registrar_sensor_instalado()
    elif opcion == "3":
        return
    else:
        print("Opción no válida")
