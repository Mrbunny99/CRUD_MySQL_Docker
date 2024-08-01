from bd_planeta.planeta_db import PlanetaDB
from bd_planeta.planeta_db import PlanetaDB
from logger.logger_config import logger

def mostrar_menu():
    """
    El menu de opciones
    """
    print("\n--- Menú de Gestión de Planetas ---")
    print("1. Crear un nuevo planeta")
    print("2. Consultar planetas")
    print("3. Actualizar un planeta")
    print("4. Eliminar un planeta")
    print("5. Salir")

def operar_bd():
    """
    Función principal que presenta un menu y realiza operaciones CRUD en la base de datos.
    """
    db = PlanetaDB(host='localhost', user='root', password='rootpassword', database='sistema_solar')

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Crear un nuevo planeta
            nombre = input("Ingrese el nombre del planeta: ")
            tipo = input("Ingrese el tipo del planeta (Rocoso, Gaseoso, etc.): ")
            radio = float(input("Ingrese el radio del planeta: "))
            distancia_sol = float(input("Ingrese la distancia del planeta al sol: "))
            db.crear(nombre, tipo, radio, distancia_sol)

        elif opcion == '2':
            # Consultar planetas
            planetas = db.leer()
            print("Lista de planetas:")
            for planeta in planetas:
                print(planeta)

        elif opcion == '3':
            # Actualizar un planeta existente
            id = int(input("Ingrese el ID del planeta a actualizar: "))
            nombre = input("Ingrese el nuevo nombre del planeta: ")
            tipo = input("Ingrese el nuevo tipo del planeta: ")
            radio = float(input("Ingrese el nuevo radio del planeta: "))
            distancia_sol = float(input("Ingrese la nueva distancia del planeta al sol: "))
            db.actualizar(id, nombre, tipo, radio, distancia_sol)

        elif opcion == '4':
            # Eliminar un planeta existente
            id = int(input("Ingrese el ID del planeta a eliminar: "))
            db.borrar(id)

        elif opcion == '5':
            # Salir del programa
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

    db.cerrar()

if __name__ == "__main__":
    operar_bd()
