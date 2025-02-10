# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
# •	Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# •	Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# •	Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# •	Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.
# SALIDA DATOS POR PANTALLA:
# Menú:
# 1. Añadir/Modificar
# 2. Buscar
# 3. Borrar
# 4. Listar
# 5. Salir
# Selecciona una opción (1-5): 1
# Introduce el nombre del contacto: Juan
# Juan no está en la agenda. Introduce el teléfono: 123456789
# Juan ha sido añadido a la agenda.

# Menú:
# 1. Añadir/Modificar
# 2. Buscar
# 3. Borrar
# 4. Listar
# 5. Salir
# Selecciona una opción (1-5): 2
# Introduce la cadena a buscar: Ju
# Contactos encontrados:
# Juan: 123456789

# Menú:
# 1. Añadir/Modificar
# 2. Buscar
# 3. Borrar
# 4. Listar
# 5. Salir
# Selecciona una opción (1-5): 3
# Introduce el nombre del contacto a borrar: Juan
# ¿Estás seguro de que quieres borrar a Juan? (sí/no): sí
# Juan ha sido borrado de la agenda.

# Menú:
# 1. Añadir/Modificar
# 2. Buscar
# 3. Borrar
# 4. Listar
# 5. Salir
# Selecciona una opción (1-5): 5
# ¡Hasta luego!



#Diccionario vacío con el que vamos a trabajar
agenda = {}


#Método para añadir o modificar, que pide algunas cuestiones al usuario, si ya existe se podrá modificar, sino añadir
def añadirModificar():
    nombre = input("Dime el nombre -->")
    if nombre in agenda:
        print("Teléfono actual de ", nombre, "es", agenda[nombre])
        modificar = input("¿Quieres modificarlo? (sí/no): ").lower()
        if modificar == "sí":
            while True:
                telefono = input("Dime el numero nuevo de teléfono -->")
                if telefono.isdigit():
                    agenda[nombre] = telefono
                    print("Teléfono de ", nombre, "actualizado")
                    break
                else:
                    print("Error, el teléfono debe ser solo numeros")
    else:
        while True:
            telefono = input("Dime el numero nuevo de teléfono -->")
            if telefono.isdigit():
                agenda[nombre] = telefono
                print("Teléfono de ", nombre, "actualizado")
                break
            else:
                print("Error, el teléfono debe ser solo numeros")


#Método para buscar,que pide algunas cuestiones al usuario, y comprueba su existencia
def buscar():
    texto = input("Dime nombre o parte de nombre para buscarlo -->").lower()
    resultados = {}
    for nombre, telefono in agenda.items():
        if nombre.lower().startswith(texto):
            resultados[nombre] = telefono
    if resultados:
        for nombre, telefono in resultados.items():
            print(nombre, telefono)
    else:
        print("No se encontraron contactos")


#Método para borrar,que pide algunas cuestiones al usuario, y comprueba su existencia
def borrar():
    nombre = input("Dime el nombre a borrar -->")
    if nombre in agenda:
        confirmar = input("¿Seguro de que le quieres borrar3? (sí/no)" ).lower()
        if confirmar == "sí":
            del agenda[nombre]
            print(nombre, "ha sido eliminado de la agenda")
    else:
        print(nombre, "no está en la agenda")


#Método para listar y comprueba su existencia
def listar():
    if agenda:
        for nombre, telefono in agenda.items():
            print(nombre, telefono)
    else:
        print("La agenda está vacía")
            

#Método main para hacer el menú de opciones, sus respectivos métodos
if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Añadir/Modificar")
        print("2. Buscar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5) -->")
        if opcion == "1":
            añadirModificar()
        elif opcion == "2":
            buscar()   
        elif opcion == "3":
            borrar()
        elif opcion == "4":
            listar() 
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else: 
            print("Opción NO correcta, prueba otras")