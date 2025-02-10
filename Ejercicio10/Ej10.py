# # Vamos a programar el juego “Mastermind”, para ello el programa debe “elegir” un número de cuatro cifras (sin cifras repetidas), que será el código que el jugador debe adivinar en la menor cantidad de intentos posibles. Cada intento consiste en una propuesta de un código posible que escribe el jugador, y una respuesta del programa. Las respuestas le darán pistas al jugador para que pueda deducir el código.
# •	Número de “MUERTOS”: Es la cantidad de dígitos que están en el número secreto y en la misma posición,
# •	Número de “HERIDOS:” Es la cantidad de dígitos que están en el número secreto, pero no en la misma posición.
# Por ejemplo, si el código que eligió el programa es el 2607, y el jugador propone el 1406, el programa le debe responder un MUERTO (el 0, que está en el código original en el mismo lugar, el tercero), y un HERIDO (el 6, que también está en el código original, pero en la segunda posición, no en el cuarto como fue propuesto).

# SALIDA DATOS POR PANTALLA:
# ¡Bienvenido al juego Mastermind!
# Tienes que adivinar un número de 4 cifras sin cifras repetidas.
# Por ejemplo, si el código es 2607 y propones 1406, la respuesta podría ser '1 MUERTO, 1 HERIDO'.
# Introduce tu intento (un número de 4 cifras sin repetir): 1234
# Resultado: 0 MUERTOS, 1 HERIDO
# Introduce tu intento (un número de 4 cifras sin repetir): 5678
# Resultado: 0 MUERTOS, 0 HERIDOS
# Introduce tu intento (un número de 4 cifras sin repetir): 2607
# Resultado: 4 MUERTOS, 0 HERIDOS
# ¡Felicidades! Has adivinado el código 2607 en 3 intentos.


#Importamos para trabajar con random
import random


#Método para jugar al juego del mastermind, donde se intenta adivinar gracias a las cuestiones lanzadas al usuario, la posición de los números
def juegoMastermind():
    print("¡Bienvenido al juego Mastermind!")
    print("Tienes que adivinar un número de 4 cifras sin cifras repetidas")
    
    numeros = list(range(10))
    codigo = ""
    intentos = 0
    adivinado = False
    
    for n in range(4):
        indice = random.randint(0, len(numeros) - 1)
        codigo += str(numeros.pop(indice))
    
    while not adivinado:
        intento = input("Dime un numero de 4 cifras sin repetir -->")
        
        if intento.isdigit() and len(intento) == 4:
            if len(set(intento)) == 4:
                intentos += 1
                muertos = 0
                for n in range(4):
                    if intento[n] == codigo[n]:
                        muertos += 1
                heridos = 0
                for n in range(4):
                    if intento[n] in codigo and intento[n] != codigo[n]:
                        heridos += 1
                
                print("Resultado: ",muertos, " MUERTOS, ", heridos, " HERIDOS")
                
                if muertos == 4:
                    print("¡Felicidades! Has adivinado el código ", codigo ,"en ",intentos ,"intentos.")    
                    
                    adivinado = True
        else:
            print("Error, debes decirme 4 cifras sin repetir")


#Método main para sus respectivos métodos
if __name__ == "__main__":
    juegoMastermind()