# Vamos a crear un programa que tenga el siguiente menú:
# 1.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3.	Longitud de la lista: te muestra el número de elementos de la lista.
# 4.	Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# 6.	Contar números: Te pide un número y te dice cuántas apariciones hay en la lista.
# 7.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# 8.	Mostrar números: Muestra los números de la lista
# 9.	Salir

# SALIDA DATOS POR PANTALLA:
# Menú:
# 1. Añadir número a la lista
# 2. Añadir número de la lista en una posición
# 3. Longitud de la lista
# 4. Eliminar el último número
# 5. Eliminar un número
# 6. Contar números
# 7. Posiciones de un número
# 8. Mostrar números
# 9. Salir
# Selecciona una opción (1-9): 1
# Introduce un número: 5
# 5 ha sido añadido al final de la lista.
# Menú:
# 1. Añadir número a la lista
# 2. Añadir número de la lista en una posición
# 3. Longitud de la lista
# 4. Eliminar el último número
# 5. Eliminar un número
# 6. Contar números
# 7. Posiciones de un número
# 8. Mostrar números
# 9. Salir
# Selecciona una opción (1-9): 6
# Introduce un número para contar sus apariciones: 5
# El número 5 aparece 1 veces en la lista.
# Menú:
# 1. Añadir número a la lista
# 2. Añadir número de la lista en una posición
# 3. Longitud de la lista
# 4. Eliminar el último número
# 5. Eliminar un número
# 6. Contar números
# 7. Posiciones de un número
# 8. Mostrar números
# 9. Salir
# Selecciona una opción (1-9): 9
# ¡Hasta luego!


#Lista vacía, con la que trabajaremos
lista = []


#Metodo para añadir un número a la lista
def añadirNumero():
    numero = int(input("Dime un numero -->"))
    lista.append(numero)
    print("El numero", numero, "ha sido añadido a la lista")


#Metodo para añadir un número a la lista, en una posicion concreta, comprobando la validez de la posición
def añadirNumeroPosicion():
    numero = int(input("Dime un numero -->"))
    posicion = int(input("Dime una posicion para añadir el numero anterior -->"))
    if posicion >= 0 and posicion <= len(lista):
        lista.insert(posicion, numero)
        print("El numero", numero, "ha sido añadido a la lista, en la posicion ", posicion)
    else:
        print("Error, posicion NO válida")


#Metodo para ver la longitud de la lista
def longitudLista():
    print("Longuitud de la lista ", len(lista))
     

#Metodo para eliminar un número a la lista, comprobando la existencia en la lista del número    
def eliminarNumero():
    if len(lista) != 0:
        borrar = lista.pop()
        print("El ultimo numero ha sido borrado de la lista")
    else:
        print("No se puede borrar nada, lista vacia")


#Metodo para eliminar un número a la lista, en una posicion concreta, comprobando la existencia en la lista del número y comprobando la validez de la posición 
def eliminarNumeroPosicion():
    if len(lista) != 0:
        posicion = int(input("Dime una posicion para borrar el numero situado en esa posicion -->"))
        if posicion >= 0 and posicion < len(lista):
            lista.pop(posicion)
            print("El numero ha sido borrado de la lista, de la posicion", posicion)
        else:
            print("Error, posicion NO válida")
    else:
        print("No se puede borrar nada, lista vacia")


#Metodo para contar el número de apariciones de dicho número en la lista
def contarNumero():
    numero = int(input("Dime un numero para ver cuantas veces está en la lista -->"))
    veces=lista.count(numero)
    print("El numero", numero, "aparece",veces,"en la lista")
 
    
#Metodo para mostrar la posicion de un número de la lista, comprobando la existencia en la lista del número
def mostrarPosicion():
    if not lista:
        print("No se puede mostrar nada, lista vacia")
        return
    
    numero = int(input("Dime un numero para ver en que posicion de la lista está -->"))
    posicion = []
    
    for n in range(len(lista)):
        if lista[n] == numero:
            posicion.append(n+1)
            
    if posicion:
        print("El numero", numero, "ha sido añadido a la lista, en la posicion", posicion)
    else:
         print("El numero", numero, "no está en la lista")


#Metodo para mostrar la lista completa de números, comprobando la existencia de números en la lista 
def mostrarNumero():
    if not lista:
        print("No se puede mostrar nada, lista vacia")
    else:
        print("Los numero de la lista son ")
        for n in lista:
            print(n)
    
    
#Método main para hacer el menú de opciones, sus respectivos métodos
if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Añadir numero a la lista")
        print("2. Añadir numero a la lista en una posición")
        print("3. Longitud de la lista")
        print("4. Eliminar el ultimo numero")
        print("5. Eliminar un numero en una posicion")
        print("6. Contarnumeros")
        print("7. Posiciones de un número")
        print("8. Mostrar números")
        print("9. Salir")
        
        opcion = input("Seleccione una opción (1-9) -->")
        
        if opcion == "1":
            añadirNumero()
        elif opcion == "2":
            añadirNumeroPosicion()
        elif opcion == "3":
            longitudLista()
        elif opcion == "4":
            eliminarNumero()
        elif opcion == "5":
            eliminarNumeroPosicion()
        elif opcion == "6":
            contarNumero()
        elif opcion == "7":
            mostrarPosicion()
        elif opcion == "8":
            mostrarNumero()
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        else: 
            print("Opción NO correcta, prueba otras")