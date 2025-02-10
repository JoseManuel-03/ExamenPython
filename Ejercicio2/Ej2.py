# Crea una función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

# SALIDA DATOS POR PANTALLA:
# Introduce una cadena: Hola, tú
# La cadena con espacios entre los caracteres: H o l a ,   t ú


#Método para poner un espacio entre letras
def convertirEspaciado(frase):
    return " ".join(texto)


#Método main para sus respectivos métodos, donde se piden que el usuario introduzca lo pedido en las cuestiones
if __name__ == "__main__":
    texto = input("Dime una frase --> ")
    print("Frase: ", convertirEspaciado(texto))