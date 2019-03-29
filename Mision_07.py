#Autor: César Guzmán Guadarrama
#
import math




def calcularDivisiones(dividiendo, divisor):
    contador = 0
    div1 = dividiendo
    dividiendo -= divisor

    while dividiendo >= 0:
        div1 -= divisor
        contador += 1

    print(dividiendo, "/", divisor, "=", contador, "Y sobran:", div1)





def encontrarMayor():
    #lista = []
    a = int(input("Teclea el número [-1 para salir]"))
    b = 0
    if a == -1:
        print("No hay valor mayor")

    while a != -1:
        if b > a:
            a = int(input("Teclea el número [-1 para salir]"))
        else:
            b = a
            a = int(input("Teclea el número [-1 para salir]"))

    print("El mayor es: ",b)



    print("""Mision 07: Ciclos while
Autor: César Guzmán Guadarrama
Matricula: A01748918
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")





        #lista.append(numero)

    #mayor = max(lista)

    #return mayor



def main():
    print("""Mision 07: Ciclos while
Autor: César Guzmán Guadarrama
Matricula: A01748918
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
    opcion = int(input("Teclea tu opcion"))

    while opcion != 0:
        if opcion == 1:
            dividiendo = float(input("¿Cual sera tu dividendo?"))
            divisor = float(input("¿Cual es tu divisor"))
            print("Calculando divisiones")
            print("Dividendo:", dividiendo)
            print("Divisor:", divisor)

            if divisor > 0:
                calcularDivisiones(dividiendo, divisor)



                print("""Mision 07: Ciclos while
Autor: César Guzmán Guadarrama
Matricula: A01748918
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")

            elif divisor < 0:
                calcularDivisiones(dividiendo, divisor)

                print("""Mision 07: Ciclos while
Autor: César Guzmán Guadarrama
Matricula: A01748918
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
            else:
                print("ERROR")

                print("""Mision 07: Ciclos while
Autor: César Guzmán Guadarrama
Matricula: A01748918
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
        elif opcion == 2:
            print("Teclea una serie de numeros para encontrar el mayor")
            encontrarMayor()
            #mayor = encontrarMayor()
            #print("El mayor es:", mayor)

        elif opcion == 3:
            print("Gracias por usar este programa, regresa pronto.")
            break
        else:
            print("ERROR")

        opcion = int(input("Teclea tu opcion"))



main()