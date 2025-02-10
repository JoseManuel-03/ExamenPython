# Crea un programa principal que permita convertir de decimal a binario y de binario a decimal.
# SALIDA DATOS POR PANTALLA:
# Seleccione una opción:
# 1. Convertir de decimal a binario
# 2. Convertir de binario a decimal
# Ingrese el número de opción (1 o 2): 1
# Ingrese un número decimal: 42
# El número 42 en binario es: 101010
# Seleccione una opción:
# 1. Convertir de decimal a binario
# 2. Convertir de binario a decimal
# Ingrese el número de opción (1 o 2): 2
# Ingrese un número binario: 101010
# El número binario 101010 en decimal es: 42



#Método para pasar de número decimal a número binario que recibe un número como parámetro
def decimalBinario(decimal):
    return bin(decimal)[2:]


#Método para pasar de número binario a número binario que recibe un número como parámetro
def binarioDecimal(binario):
    return int(binario, 2)


#Método main para hacer el menú de opciones,con sus respectivos métodos, donde se piden que el usuario introduzca lo pedido en las cuestiones
if __name__ == "__main__":
    while True:
        print("Seleccione una opción (1-3) -->")
        print("1. Pasar de decimal a binario")
        print("2. Pasar de binario a decimal")
        print("3. Salir")
        
        opcion = input("Dime el numero de opción (1,2 o 3) -->")
        
        if opcion == "1":
            try:
                numeroDecimal = int(input("Dime un número decimal -->"))
                numeroBinario = decimalBinario(numeroDecimal)
                print("El número", numeroDecimal, "en binario es: ", numeroBinario)
            except ValueError:
                print("Error, debe ingresar un número decimal válido")
        elif opcion == "2":
            numeroBinario = input("Dime un número binario: ")
            numeroDecimal = binarioDecimal(numeroBinario)
            for caracter in numeroBinario:
                if(caracter not in "01"):
                    print("Error, debe ingresar un número decimal válido, debe ser 0 o 1")
                    break
            print("El número binario", numeroBinario, "en decimal es: ", numeroDecimal)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else: 
            print("Opción NO correcta, prueba otras")
            