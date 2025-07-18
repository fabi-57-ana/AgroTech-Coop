
from gestion_parcelas import menu_parcelas
from gestion_sensores import menu_sensores
from registro_mediciones import menu_mediciones
from consulta_datos import menu_consultas

def mostrar_menu_principal():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Gestión de Parcelas")
    print("2. Gestión de Sensores")
    print("3. Registro de Mediciones")
    print("4. Consulta de Datos")
    print("5. Salir")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_parcelas()
        elif opcion == "2":
            menu_sensores()
        elif opcion == "3":
            menu_mediciones()
        elif opcion == "4":
            menu_consultas()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()