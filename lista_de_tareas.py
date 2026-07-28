# Lista donde guardaremos las tareas
tareas = []

while True:
    print("\n--- MI LISTA DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("\nElige una opción (1-4): ")

    if opcion == "1":
        # TODO: Si la lista está vacía, avisa al usuario.
        # Si tiene tareas, muéstralas numeradas (1. Tarea A, 2. Tarea B...)
        if len(tareas) == 0:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == "2":
        # TODO: Pide al usuario el nombre de la nueva tarea y añádela a la lista
        nueva_tarea = input("Introduce la nueva tarea: ")
        tareas.append(nueva_tarea)

    elif opcion == "3":
        # TODO: Muestra las tareas para que sepa cuál borrar,
        # pide el número de tarea y elimínala de la lista.
        if len(tareas) == 0:
            print("No tienes tareas pendientes")
        else:
            while True:
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea}")
                num = int(input("Introduce el numero de la tarea que deseas eliminar:"))
                n_tareas = len(tareas)
                if 1 <= num <= n_tareas:
                    print("Estas seguro de que quieres eliminarlo?")
                    print("Escribe Si/No")
                    respuesta0 = input()
                    respuesta1 = respuesta0.lower()
                    if respuesta1 == "si":
                        tarea_eliminada = tareas.pop(num-1)
                        print(f"La tarea {tarea_eliminada} ha sido eliminada")
                        break
                    else:
                        break
                else:
                    print("---------------------")
                    print("Numero no valido, intente de nuevo")
                    print("---------------------")
            
    elif opcion == "4":
        print("¡Hasta luego! Guardando tareas...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")