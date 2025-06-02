
def visualizar_datos():
    print("\nFunción visualizar_datos() invocada")

def menu_consultas():
    print("\n=== CONSULTA DE DATOS ===")
    print("1. Visualizar datos")
    print("2. Volver al menú principal")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        visualizar_datos()
    elif opcion == "2":
        return
    else:
        print("Opción no válida")
