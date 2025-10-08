def menu(): 
    print("// Bienvenido a su diccionario //")
    print("1. Agregar videojuego")
    print("3. Mostrar diccionario")
    print("4. Salir")

def agregar_videojuego(diccionario):
        videojuego = input("Ingrese el nombre del videojuego: ")
        descripcion = input("Ingrese la descripcion del videojuego: ")
        genero = input("Ingrese el genero del videojuego: ")
        puntuacion = input("Ingrese la puntuacion del videojuego: ")
        diccionario[videojuego] = {"descripcion": descripcion, "genero": genero, "puntuacion": puntuacion}

def mostrar_diccionario(diccionario):
    print("Diccionario de videojuegos:")
    print(diccionario)

def main():
    diccionario = {}
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            agregar_videojuego(diccionario)
        elif opcion == "3":
            mostrar_diccionario(diccionario)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intente de nuevo.")
main()