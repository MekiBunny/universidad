def menu():
  print("Bienvenido al sistema")
  print("1- Agregar estudiante")
  print("2-Ver promedio de un estudiante")
  print("3-Editar nota de un estudiante")
  print("4-Ver reprobados")
  print("5-Ver aprobados")
  print("6-Salir" )

def agregar_estudiante(diccionario):
  estudiante = input("Ingrese el nombre del estudiante: ")
  nota1 = float(input("Ingrese la primera nota: "))
  nota2 = float(input("Ingrese la segunda nota: "))
  nota3 = float(input("Ingrese la tercera nota: "))
  diccionario[estudiante] = [nota1, nota2, nota3]

def ver_promedio_estudiante(diccionario):
  estudiante = input("Ingrese el nombre del estudiante: ")
  if estudiante in diccionario:
    notas = diccionario[estudiante]
    promedio = notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4
    return f"{promedio:.2f}"
  else:
    print("Estudiante no encontrado.")

def ver_reprobados(diccionario):
  reprobados = []
  for estudiante, notas in diccionario.items():
    promedio = notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4
    if promedio < 3.0: 
       reprobados.append((estudiante, (promedio)))
  return reprobados

def ver_aprobados(diccionario):
  aprobados = []
  for estudiante, notas in diccionario.items():
    promedio = notas[0] * 0.3 + notas[1] * 0.3 + notas[2] * 0.4
    if promedio >= 3.0:
       aprobados.append((estudiante, (promedio)))
  return aprobados

def editar_nota(diccionario):
  estudiante = input("Ingrese el nombre del estudiante: ")
  if estudiante in diccionario:
    print("Notas actuales:", diccionario[estudiante])
    nota_num = int(input("Ingrese el numero de la nota a editar (1, 2 o 3): "))
    if nota_num in [1, 2, 3]:
      nueva_nota = float(input("Ingrese la nueva nota: "))
      diccionario[estudiante][nota_num - 1] = nueva_nota
      print("Nota actualizada.")
    else:
      print("Numero de nota invalido.")
  else:
    print("Estudiante no encontrado.")

def main():
  diccionario = {}
  while True:
    menu()
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
      agregar_estudiante(diccionario)
    elif opcion == "2":
      promedio = ver_promedio_estudiante(diccionario)
      if promedio is not None:
        print("El promedio del estudiante es:", promedio)
    elif opcion == "3":
      editar_nota(diccionario)
    elif opcion == "4":
        reprobados = ver_reprobados(diccionario)
        if reprobados:
            print("Los reprobados son:", reprobados)
        else:
            print("No hay estudiantes reprobados.")
    elif opcion == "5":
      aprobados = ver_aprobados(diccionario)
      if aprobados:
        print("Los aprobados son:", aprobados)
      else:
        print("No hay estudiantes aprobados.")
    elif opcion == "6":
      print("Saliendo del programa...")
      break
    else:
      print("Opcion no valida, intente de nuevo.")
main()