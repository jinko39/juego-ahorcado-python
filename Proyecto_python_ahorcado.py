########## 
pistas = {
    "elefante": "animal grande con trompa",
    "servilleta": "la tenes a la hora de comer al lado del plato",
    "golf": "deporte con cancha de hoyos que juega la gente con plata",
    "colegio": "lugar donde vas a aprender, estudiar y socializar",
    "otorrinolaringologo": "médico o médica de oídos, nariz y garganta"
    }


import random


def obtener_palabra_random():
    palabras = ["otorrinolaringologo" , "elefante" , "servilleta", "colegio" , "golf"] #sabemos q otorrinolaringólogo va con tilde ok??
    palabra_random=random.choice(palabras)
    return palabra_random
    

def mostrar_tablero(palabra_secreta,letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero += "_"
    print(tablero)

def mostrar_instrucciones():
    """Explica las reglas del juego."""
    print("\n--- CÓMO SE JUEGA ---")
    print("1. Se elige una palabra secreta al azar.")
    print("2. Tirás letras de a una.")
    print("3. Si la letra está en la palabra, se descubre.")
    print("4. Si no está, perdés un intento. Tenés 6.")
    print("5. Si te quedás sin intentos, perdés. ¡Suerte!")
    print("----------------------")
    input("Presione cualquier tecla para continuar.")
# /n es para salto de línea

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_random()
    letras_adivinadas = []
    intentos_restantes = int(6) 

    while intentos_restantes>0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("introduce una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya has introducido esta letra, probá otra: ")
            continue
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta):
                print("Felicitaciones! Ganaste! :)")
                break

        else:
            intentos_restantes -=1
            print(f"Letra incorecta... Te quedan:", intentos_restantes)
            if intentos_restantes >= 1 :
                respuesta = input("¿Querés una pista? (si/no): ").lower()
                while respuesta != "si" and respuesta != "no":
                    respuesta = input("No te entendí, intentá de nuevo!: ").lower()
                if respuesta == "si": 
                    print("Pista:", pistas[palabra_secreta])
            

    if intentos_restantes==0:
        print("Perdiste :( , la palabra secreta era:", palabra_secreta)


def mostrar_menu():
    """Menú principal: jugar, ver instrucciones o salir."""
    while True:
        print("\n=== AHORCADO ===")
        print("1. Jugar")
        print("2. Cómo se juega")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            jugar_ahorcado()
        elif opcion == "2":
            mostrar_instrucciones()
        elif opcion == "3":
            print("Gracias por jugar!")
            break
        else:
            print("Opción inválida, probá de nuevo.")


mostrar_menu()






# 