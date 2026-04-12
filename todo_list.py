def mostrar_menu():
    print("=== Lista de Tareas ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")

def main():
    tareas = []
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            tarea = input("Nueva tarea: ")
            tareas.append(tarea)
            print("Tarea agregada.")
        elif opcion == "2":
            if not tareas:
                print("No hay tareas.")
            else:
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t}")
        elif opcion == "3":
            print("Adiós!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
