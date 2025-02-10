# Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.
# Vamos a crear las siguientes funciones para trabajar con funciones:
# •	Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
# •	Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
# •	Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
# •	Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# •	Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# •	Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# •	Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
# •	Usar la librería fractions de Python

# Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
# 1.	Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
# 2.	Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
# 3.	Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto.
# 4.	Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra el cociente.
# 5.	Salir

# SALIDA DATOS POR PANTALLA:

# Menú:
# 1. Sumar dos fracciones
# 2. Restar dos fracciones
# 3. Multiplicar dos fracciones
# 4. Dividir dos fracciones
# 5. Salir
# Seleccione una opción: 1
# Introduce el numerador de la primera fracción: 1
# Introduce el denominador de la primera fracción: 2
# Introduce el numerador de la segunda fracción: 1
# Introduce el denominador de la segunda fracción: 3
# El resultado de la suma es: 5/6



#Importamos para trabajar con fracciones
from fractions import Fraction


#Método para leer una fracción que pide un numerador y denominador, comprabando su validez
def leer_fracción():
    numerador = int(input("Dime numerador -->"))
    denominador = int(input("Dime denominador -->"))
    if numerador == 0:
        print("Numerador no puede ser 0")
        numerador = int(input("Dime numerador de nuevo -->"))
    if numerador == 0 and denominador == 0:
        print("0/0, no es posible")
        numerador = int(input("Dime numerador -->"))
        denominador = int(input("Dime denominador -->"))
    if denominador == 0:
        print("Numerador no puede ser 0")
        denominador = int(input("Dime denominador de nuevo -->"))
    return Fraction(numerador, denominador)


#Método para escribir una fracción que representa cómo se escribe correctamente
def escribir_fracción(fraccion):
    if fraccion.denominator==1:
        print(fraccion.numerator)
    else:
        print(fraccion.numerator/fraccion.denominator)


#Método para simplificar fraccion utilizando Fraction
def simplificar_fracción(fraccion):
    return Fraction(fraccion.numerator,fraccion.denominator)


#Método para sumar fracciones(con el operador +)
def sumar_fracciones(fraccion1, fraccion2):
    return fraccion1+fraccion2


#Método para restar fracciones(con el operador -)
def restar_fracciones(fraccion1, fraccion2):
    return fraccion1-fraccion2


#Método para multiplicar fracciones(con el operador *)
def multiplicar_fracciones(fraccion1, fraccion2):
    return fraccion1*fraccion2


#Método para dividir fracciones(con el operador /)
def dividir_fracciones(fraccion1, fraccion2):
    return fraccion1/fraccion2


#Método main para hacer el menú de opciones, sus respectivos métodos
if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Sumar dos fracciones")
        print("2. Restar dos fracciones")
        print("3. Multiplicar dos fracciones")
        print("4. Dividir dos fracciones")
        print("5. Salir")
        opcion = input("Seleccione una opción  (1-5) -->")
        
        if opcion == "5":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        elif opcion in ("1","2","3","4"):
            print("Primera fracción")
            fraccion1 = leer_fracción()
            print("Segunda fracción")
            fraccion2 = leer_fracción()
            
            if opcion == "1":
                print("Suma -->")
                escribir_fracción(sumar_fracciones(fraccion1, fraccion2)) 
            elif opcion == "2":
                print("Resta -->")
                escribir_fracción(restar_fracciones(fraccion1, fraccion2))
            elif opcion == "3":
                print("Multiplicación -->")
                escribir_fracción(multiplicar_fracciones(fraccion1, fraccion2))
            elif opcion == "4":
                print("Division -->")
                escribir_fracción(dividir_fracciones(fraccion1, fraccion2))
        else: 
            print("Opción NO correcta, prueba otras")