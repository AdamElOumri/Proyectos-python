
import random

palabras = ["python", "programacion", "computadora", "desarrollador", "teclado"]
fotograma1 = ("___________","  |      ||","  |      ||","         ||","         ||","         ||","       |¯¯¯¯¯¯¯¯¯¯¯|","       |ˍˍˍˍˍˍˍˍˍˍˍ|")
fotograma2 = ("___________","  |      ||","  |      ||","  O      ||","         ||","         ||","       |¯¯¯¯¯¯¯¯¯¯¯|","       |ˍˍˍˍˍˍˍˍˍˍˍ|")
fotograma3 = ("___________","  |      ||","  |      ||","  O      ||","  |      ||","         ||","       |¯¯¯¯¯¯¯¯¯¯¯|","       |ˍˍˍˍˍˍˍˍˍˍˍ|")
fotograma4 = ("___________","  |      ||","  |      ||","  O      ||"," /|      ||","         ||","       |¯¯¯¯¯¯¯¯¯¯¯|","       |ˍˍˍˍˍˍˍˍˍˍˍ|")
fotograma5 = ("___________","  |      ||","  |      ||","  O      ||"," /|\\     ||","         ||","       |¯¯¯¯¯¯¯¯¯¯¯|","       |ˍˍˍˍˍˍˍˍˍˍˍ|")
fotograma6 = ("___________","  |      ||","  |      ||","  O      ||"," /|\\     ||"," /       ||","       |¯¯¯¯¯¯¯¯¯¯¯|","       |ˍˍˍˍˍˍˍˍˍˍˍ|")
fotograma7 = ("___________","  |      ||","  |      ||","  O      ||"," /|\\     ||"," / \\     ||","       |¯¯¯¯¯¯¯¯¯¯¯|","       |ˍˍˍˍˍˍˍˍˍˍˍ|")
animacion = [fotograma1,fotograma2,fotograma3,fotograma4,fotograma5,fotograma6,fotograma7]

while True:
    print("Bienvenido al juego del ahoracado!!!")
    print("  Jugar")
    print("  Salir")
    accion = input("Que quieres hacer?").lower()
    
    if accion == "jugar":
        print("COMENCEMOS!!!")
        palabra_secreta = ps = random.choice(palabras).lower()
        n_letras = len(palabra_secreta)
        palabra_secreta_oculta = pso = "_" * n_letras
        letras_buenas = []
        letras_malas = []
        indices = []
        vidas_actuales = ["♥","♥","♥","♥","♥","♥"]
        a = 0

        while True:
            imagen = animacion[a]
            for _ in imagen:
                print(_)

            print(vidas_actuales)
            print(letras_buenas)
            print(letras_malas)
            print(pso)
            letra = input("Introduce una letra: ")    
            if letra in ps:
                print("Muy Bienn!")
                letras_buenas.append(letra)
                n_iteraciones = 0
                for b in ps:
                    if b == letra:
                        indices.append(n_iteraciones)
                    n_iteraciones = n_iteraciones + 1

                for indice in indices:      
                    pso = pso[:indice] + letra + pso[indice+1:]
                indices.clear()
                
                if "_" not in pso:
                    print(f"\n¡¡¡GANASTE!!! Has adivinado la palabra: {pso}")
                    break
                
            else:
                print("Casi!")
                print("-1♥")
                letras_malas.append(letra)
                vidas_actuales.pop(-1)
                a = a + 1
                if len(vidas_actuales) == 0:
                    imagen = animacion[a]
                    for _ in imagen:
                        print(_)
                    print("Perdiste...")
                    print(f"La palabra era {ps}")
                    break
                continue

    elif accion == "salir":
        break
    else:
        continue
        
        
        