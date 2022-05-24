import time
clase = []
promedio_clase = []
i = True


def menu():
    print("Seleccione la opción que desee realizar: ")
    time.sleep(1)
    print()
    print()
    print("1)  Ingresar notas de la clase. \n"
          "2)  Calcular promedio de la clase. \n"
          "3)  Ver promedio. \n"
          "4)  Ver notas de la clase. \n"
          "5)  Limpiar notas y promedio. \n"
          "6)  Salir.")
    print()
    opcion = input(" ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6":
        opcion = input("Seleccione un número válido: ")
    if opcion == "1":
        notas()
    elif opcion == "2":
        prom()
    elif opcion == "3":
        ver_promedio()
    elif opcion == "4":
        ver_notas()
    elif opcion == "5":
        limpiar_nyt()
    elif opcion == "6":
        salir()


def notas():
    i = True
    while i:
        try:
            n = float(input("Ingrese la nota: "))
        except ValueError:
            print("")
            continue
        if n == 123:
            i = False
            print()
            print("Las notas de la clase son: ", clase)
            time.sleep(2)
            print()
            print("Regresando al menú...")
            time.sleep(2)
            print()
            menu()
        elif n < 0 or n > 20:
            print("Ingrese una nota válida.")
            continue
        else:
            clase.append(n)


def prom():

    if clase == []:
        print("Las notas de clase están vacías, por favor, ingrese las notas para poder promediar.")
        time.sleep(2)
        print("Regresando al menú...")
        time.sleep(2)
        print()
        menu()
        print()
    else:
        promedio = sum(clase) / len(clase)
        print("Calculando promedio, por favor, espere...")
        time.sleep(2)
        promedio_clase.append(promedio)
        print("El promedio de la clase es de: ", promedio)
        time.sleep(2)
        print("Regresando al menú...")
        time.sleep(2)
        menu()
        print()


def ver_promedio():


    if promedio_clase == []:
        print("El promedio de la clase está vacío, por favor, ingrese notas y promedie para poder verlo.")
        print()
        print("Regresando al menú...")
        time.sleep(2)
        print()
        menu()
        print()
    else:
        print("El promedio de la clase es de: ", promedio_clase)
        time.sleep(2)
        print("Regresando al menú...")
        time.sleep(2)
        menu()
        print()


def ver_notas():

    if clase == []:
        print("Las notas de clase están vacías, por favor, colóquelas para poder visualizarlas")
        time.sleep(2)
        print("Regresando al menú...")
        time.sleep(1)
        print()
        menu()
    else:
        print("Las notas de la clase son: ", clase)
        time.sleep(2)
        print("Regresando al menú...")
        time.sleep(2)
        menu()
        print()


def limpiar_nyt():

    if clase == [] and promedio_clase == []:

        print("Complete notas o promedio para poder limpiar.")
        print()
        time.sleep(2)
        print("Regresando al menú...")
        time.sleep(2)
        print()
        menu()

    else:
        print()
        print("Las notas y promedio se limpiarán en un momento, espere...")
        time.sleep(2)
        del clase[:]
        del promedio_clase[:]
        print()
        print("Las notas y promedio se limpiaron correctamente.")
        time.sleep(2)
        print()
        print("Regresando al menú...")
        print()
        time.sleep(1)
        menu()


def salir():

    while i:
        print()
        print("Saliendo, hasta luego.")
        break



print("Bienvenido profesor/a")
print()
time.sleep(2)
menu()
