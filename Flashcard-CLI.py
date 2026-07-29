import random


tarjetas = {
    "¿Cuál es la capital de España?": "Madrid",
    "¿Qué comando se usa para clonar un repositorio?": "git clone",
    "¿Cómo se añade un elemento a una lista en Python?": ".append()"
}

textos = ("---FLASHCARDS---","¿Qué deseas hacer?","  1.Ponte a prueba","  2.Mostrar flashcards","  3.Añadir flashcard","  4.Salir", "Escribe solo el numero")
while True:
    
    for texto in textos:
        print(texto)
    opcion = input("Introduce la opcion: ")
    if opcion == "1":
        while True:

            preguntas = list(tarjetas.keys())
            
        
            pregunta = random.choice(preguntas)
            respuesta_correcta = tarjetas[pregunta]
            
            print("\nPregunta:")
            print(pregunta)
            
            respuesta_usuario = input("Escribe la respuesta: ")
            
            if respuesta_usuario.strip().lower() == respuesta_correcta.lower():
                print("Has acertado!!!")
            else:
                print(f"La respuesta correcta era: {respuesta_correcta}")
                
            seguir = input("\n¿Continuamos? (S/N): ").lower()
            if seguir != "s":
                break
            
    elif opcion == "2":
        
        print("\n---Todas Las Flashcards---")
        for clave,valor in tarjetas.items():
            print(f"• P:{clave} ---> R:{valor}")
            

    elif opcion == "3":
        pregunta_nueva = input("Introduce la nueva pregunta")
        respuesta_nueva = input("Introduce la respuesta")
        tarjetas[pregunta_nueva] = respuesta_nueva
        print("Guardando...")

    elif opcion == "4":
        print("¡Gracias por estudiar! ¡Hasta la próxima!")
        
        break
    else:
        print("Opción no válida.")