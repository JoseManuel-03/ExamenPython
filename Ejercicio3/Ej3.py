# Vamos a crear un programa en Python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
#  El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los 
#  datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

# # SALIDA DATOS POR PANTALLA:
# Introduce el nombre de la fruta: manzana
# Introduce la cantidad vendida: 3
# El precio total de 3.0 kg de manzana es: 3.6€

# ¿Quieres hacer otra consulta? (sí/no): sí
# Introduce el nombre de la fruta: pera
# Error: La fruta pera no está disponible en el diccionario.

# ¿Quieres hacer otra consulta? (sí/no): no
# Gracias por usar el programa. ¡Hasta luego!


#Diccionario que contiene el nombre de la fruta y su respectivo precio, con el que vamos a trabajar
precioFrutas = {
    "banana": 0.4,
    "naranja":0.8,
    "manzana":1.1,
    "uva":0.6
}


#Método para calcular el precio en € de una fruta
def calcularPrecio(fruta, cantidad):
    if fruta in precioFrutas:
        total = precioFrutas[fruta] * cantidad
        print("El precio total de " ,cantidad ," kg de ",fruta ," es: " ,total, " €" )
    else:
        print("Error: La fruta no está disponible en el diccionario")


#Método main para sus respectivos métodos, donde se piden que el usuario introduzca lo pedido en las cuestiones
if __name__ == "__main__":
    while True:
        fruta = input("Nombre de una fruta -->")
        try:
            cantidad = float(input("Cantidad vendida en kg -->"))
            calcularPrecio(fruta, cantidad)
        except ValueError:
            print("Error, cantidad errónea")
        
        while True:
            otraConsulta = input("¿Quieres hacer otra consulta? (sí/no) -->")
            if otraConsulta == "sí":
                break
            elif otraConsulta == "no":
                print("Gracias por usar el programa. ¡Hasta luego!")
                exit()
            else:
                print("Responde con sí o con no")
                