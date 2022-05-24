Lo que hice al principio del código primero fue importar time para que pueda usar un retraso por segundos para que la aplicación se vea más "realista".
Luego declaré variables, clase y promedio clase como listas vacías, la variable i como True para que luego podamos usarla.

import time
clase = []
promedio_clase = []
a = True

Empezando con las funciones, lo que hice fue crear una llamada menu, la cual servirá para meter todas las demás funciones y regrese al menú una vez cada funcion termine de hacer su trabajo, las funciones en total fueron 6 las cuales son:

Ingresar notas de la clase
Calcular promedio de la clase
Ver promedio
Ver notas de la clase
Limpiar notas y promedio
Salir

Dichas opciones, saldrán como un print, así como también un print que nos dirá que seleccionemos las opciones que deseemos realizar, (Los prints vacíos sirven para tener un espacio considerable entre cada print).

Luego delcaré la variable opción como un input con string vacío, para que se vea más ordenado al momento de poner la opción que deseemos realizar.
Luego usé un while, el cual sirve para hacer restricciones, si los números ingresados en la variable opcion no son ni 1, 2, 3, 4, 5 o 6, saldrá nuevamente un input que diga "Seleccione un número válido" hasta que pongamos un número del 1 al 6.

Si la variable "opcion" toma como valor 1, se ejecutará la función "notas", la cual sirve para ingresar las notas de la clase, si es 2, ejecutará la opción "prom" la cual sirve para promediar todas las notas, si es 3, se podrá visualizar el promedio y se ejecutará la función "ver_promedio", si es 4, se ejecuta la función "ver_notas" para ver todas las notas actuales de la clase, si es 5, se ejecuta la función "limpiar_nyt" la cual sirve para limpiar notas y promedio y se puedan ingresar nuevos valores, y finalmente, si la opción es 6, se sale de la aplicación.

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
        
Luego definí cómo iba a ser el código de la función "notas", en donde uso una variable auxiliar "i" para poder hacer un bucle con while, así como también usé los comandos try y except, ya que, nos pedirá ingresar notas, las cuales pueden ser ingresadas con decimales, pero no menores a 0 ni mayores a 20, al solo poder ingresar números, dará un error si se ingresa un string, así que, usé try que para cuando se ejecute esa línea de código y como resultado de un ValueError, imprima "Ingrese una nota válida" y vuelva a ejecutarse esa línea de código.
Para romper el bucle, lo único que se tiene que hacer es digitar 123, dar enter y nuestra variable auxiliar pasará ser False, rompiendo con el bucle while, añade todas las notas a nuestra lista vacía llamada "clase" y volverá al menú.

En la función promedio lo que hice al principio es que si esta es ejecutada y las notas de clase están vacías, imprima que las notas estén vacías y que las digite para poder promediar, regresándonos al menú, y si las notas están rellenadas, suma todos los valores dentro de la lista clase y los divide entre la cantidad de valores que hay, dándonos al final cuál es el promedio de la clase, añadiéndolo a la lista vacía "promedio_clase" y luego nos regresa al menú.

Lo mismo hice al inicio de la función "ver_promedio", en caso de que la lista "promedio_clase" esté vacía, no se podrá visualizar el promedio, saliendo un print que nos dirá que el promedio de la clase esté vacío, que ingresemos notas y quye promediemos para poder verlo, lo único que hace esta función es digitalizar cuál es el promedio y regresándonos al menú, lo mismo ocurre con la función "ver_notas".

Para la función "limpiar_nyt" Lo que hice fue que en caso de que tanto notas como promedio estén vacías, imprima, no hay nada para limpiar, y nos regrese al menú.
Si este no fuese el caso, imprime que las notas y promedio se limpiarán, usé el comando del para poder eliminar todos los elementos de la lista "clase" y "promedio_clase", seleccionando todos sus elementos por medio del index: [:]
Luego de limpiar, nos regresa al menú.

Finalmente, para la función salir, usé la variable auxiliar que definí al inicio del código, la cual es a = True.
Al ejecutar la función salir, lo que hace es usar un while, que, mientras "a" sea verdadero, imprima "Saliendo, hasta luego", para que luego rompa con el código.
Al final puse cómo incia el código, solo imprimiendo "Bienvenido profesor/a" y mandándonos al menú.
