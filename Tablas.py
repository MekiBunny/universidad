def tablas(tabla: int, desde: int, hasta: int) -> None:
    for i in range(desde, hasta,  1):
        print(f"{tabla} x {i} = {tabla * i}")


tabla = int(input("Ingrese la tabla de multiplicar que quiere conocer: "))
desde = int(input("Ingrese desde que número desea conocer "))
hasta = int(input("Ingrese hasta que número desea conocer "))
tablas(tabla, desde, hasta)