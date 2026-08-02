import os
import pandas as pd

def menu():
    print("ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ")
    print("|   ---GESTOR DE GASTOS---   |")
    print("|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
    print("|  ☼¿Qué te gustaría hacer?☼ |")
    print("|    1. Añadir gasto         |")
    print("|    2. Mirar gastos         |")
    print("|    3. Ver total y resumen  |")
    print("|    4. Salir                |")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

archivo = "gastos.csv"

if not os.path.exists(archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("producto,precio(€),categoria\n")

while True:
    menu()
    opcion = str(input("¿Qué quieres hacer? (1-4):\n"))

    if opcion == "1":
        nombre_producto = input("¿Qué producto era?:\n")
        precio = input("¿Cuánto te gastaste?:\n")  
        
        print("Categorías:\nAlimentacion  Compras  Salud  Casa  Créditos  Restaurantes  Otros  Más")
        tg = input("Selecciona categoría: ").lower()
        
        if tg in ["más", "mas"]:
            tg = input("Introduce la nueva categoría:\n")

        linea_csv = f"{nombre_producto},{precio},{tg}\n"
        
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(linea_csv)
            
        print("Gasto añadido con éxito\n") 

    elif opcion == "2":
        if os.path.exists(archivo):
            df = pd.read_csv(archivo)
            print("\n--- TUS GASTOS ---")
            print(df)
            print("------------------\n")
        else:
            print("No hay datos todavía.")

    elif opcion == "3":
        if os.path.exists(archivo):
            df = pd.read_csv(archivo)
            total = df["precio"].sum()
            print(f"\nTu gasto total ha sido de: {total}€")
            lista_categorias = df['categoria'].unique().tolist()
            valores = " -- ".join(lista_categorias)
            categoria0 = input(f"\nElige qué categoría quieres ver:\n[{valores}]\nCategoría: ").lower()
            
            if categoria0 not in lista_categorias:
                print("No existe esa categoría en el registro.\n")
            else:
                gasto_categoria = df[df["categoria"] == categoria0]["precio"].sum()
                print(f"Has gastado un total de {gasto_categoria}€ en la categoría '{categoria0}'.\n")
        else:
            print("No hay datos registrados aún.")

    elif opcion == "4":
        print("¡Hasta la próxima!")
        break
    else:
        print("Caracter no válido, inténtalo de nuevo.\n")
        
        

            
        
            
    
    
            

            
                