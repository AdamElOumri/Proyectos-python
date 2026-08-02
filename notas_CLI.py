import os

nombre_archivo = "notas.txt"
notas = []

if os.path.exists(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea: continue
            partes = linea.split(":", 1)
            if len(partes) == 2:
                notas.append((partes[0], partes[1]))

textos = ("---Bloc De Notas---", "¿Qué te gustaria hacer?", " 1. Mirar notas", " 2. Añadir nota", " 3. Eliminar nota", " 4. Salir", "Selecciona una opcion \n(elige un numero):")

while True:
    for _ in textos:
        print(_)
    n = input()

    if n == "1":
        if not notas:
            print("No hay notas guardadas.")
        else:
            for titulo, cuerpo in notas:
                print(f"--Título:--\n {titulo}\n--Cuerpo:-- \n{cuerpo}")

    elif n == "2":
        titulo = input("Introduce el titulo de la nota: ")
        cuerpo = input("Introduce el cuerpo de la nota: ")
        notas.append((titulo, cuerpo))
        print("La nota ha sido guardada correctamente (en memoria).")

    elif n == "3":
        if not notas:
            print("No hay notas para eliminar.")
        else:
            print("---Notas actuales---")
            for titulo, cuerpo in notas:
                print(f"--Título:--\n {titulo}\n--Cuerpo:-- \n{cuerpo}")
            nota_eliminar = input("Introduce el titulo de la nota que deseas eliminar:\n")
            notas_antes = len(notas)
            notas = [nota for nota in notas if nota[0] != nota_eliminar]
            
            if len(notas) < notas_antes:
                print("Nota eliminada de la lista.")
            else:
                print("No se encontró ninguna nota con ese título.")

    elif n == "4":
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            for titulo, cuerpo in notas:
                f.write(f"{titulo}:{cuerpo}\n")
        print("Cambios guardados en el archivo. Saliendo...")
        break
    else:
        print("caracter no valido \nintentalo de nuevo")   

