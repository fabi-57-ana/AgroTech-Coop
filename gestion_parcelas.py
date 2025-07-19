from conexion_db import get_db_connection
import mysql.connector


def registrar_parcela():
    conn = get_db_connection()
    if not conn:
        return
    
    cursor = conn.cursor(dictionary=True)
    
    print("\n=== REGISTRAR NUEVA PARCELA ===")
    nombre = input("Nombre de la parcela: ")
    ubicacion = input("Ubicación: ")
    area = float(input("Área en m²: "))
    
    # Mostrar cultivos disponibles
    cursor.execute("SELECT id_cultivo, nombre FROM cultivos")
    cultivos = cursor.fetchall()
    
    print("\nCultivos disponibles:")
    for cultivo in cultivos:
        print(f"{cultivo['id_cultivo']}. {cultivo['nombre']}")
    
    id_cultivo = int(input("ID del cultivo: "))
    
    try:
        cursor.execute(
            "INSERT INTO parcelas (nombre, ubicacion, area, id_cultivo) VALUES (%s, %s, %s, %s)",
            (nombre, ubicacion, area, id_cultivo)
        )
        conn.commit()
        print("Parcela registrada exitosamente!")
    except mysql.connector.Error as err:
        print(f"Error al registrar parcela: {err}")
    finally:
        cursor.close()
        conn.close()

def listar_parcelas():
    conn = get_db_connection()
    if not conn:
        return
    
    cursor = conn.cursor(dictionary=True)
    
    print("\n=== LISTADO DE PARCELAS ===")
    cursor.execute("""
        SELECT p.id_parcela, p.nombre, p.ubicacion, p.area, c.nombre as cultivo 
        FROM parcelas p 
        JOIN cultivos c ON p.id_cultivo = c.id_cultivo
    """)
    
    parcelas = cursor.fetchall()
    
    if not parcelas:
        print("No hay parcelas registradas.")
    else:
        for parcela in parcelas:
            print(f"\nID: {parcela['id_parcela']}")
            print(f"Nombre: {parcela['nombre']}")
            print(f"Ubicación: {parcela['ubicacion']}")
            print(f"Área: {parcela['area']} m²")
            print(f"Cultivo: {parcela['cultivo']}")
    
    cursor.close()
    conn.close()

def menu_parcelas():
    while True:
        print("\n=== GESTIÓN DE PARCELAS ===")
        print("1. Registrar nueva parcela")
        print("2. Listar parcelas registradas")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_parcela()
        elif opcion == "2":
            listar_parcelas()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")
