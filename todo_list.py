def mostrar_menu():
    print("=== Lista de Tareas ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")

def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas.")
        return
    for i, t in enumerate(tareas, 1):
        print(f"{i}. {t}")
    try:
        num = int(input("Número de tarea a marcar: "))
        if 1 <= num <= len(tareas):
            tarea = tareas.pop(num - 1)
            print(f"Tarea '{tarea}' marcada como completada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

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
            marcar_completada(tareas)
        elif opcion == "4":
            print("Adiós!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
