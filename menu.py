#crear menu con 3 opciones: 1. Numeros 2. Personas 3. Finalizar
import os
def Numeros():
    #ingresar n numeros donde n es un numero ingresado por el usuario
    #mostrar la cantidad de numeros positivos, negativos e igual a 0
    veces=int(input("Cuantos números ingresa?: "))
    positivos=0
    negativos=0
    igualcero=0
    for x in range(veces):
        nume=int(input("Ingrese un número: "))
        if (nume>0):
            positivos=positivos+1
        elif(nume<0):
            negativos=negativos+1
        elif(nume==0):
            igualcero=igualcero+1     
    print("Numero/s positivo/s: "+str(positivos))
    print("Numero/s negativo/s: "+str(negativos))
    print("Numero/s iguale/s a 0: "+str(igualcero))
    pausa=input("Presione una tecla para continuar..")

def Personas():
    #ingresar nombre y edad para n personas. N es un numero ingresado por teclado
    #mostrar: promedio de todas las edades ingresadas
    n=int(input("Digite numero de personas a ingresar: "))
    a=0
    sum=0
    for i in range(n):
        nom=input("Ingrese nombre de la persona: ")
        a=int(input("Ingrese la edad de la perdsona: "))
        sum=sum+a

    print("Promedio de las edades: " + str(sum/n))
    pausa=input("Presione una tecla para continuar..")

seguir=True
while seguir:
    os.system('cls')
    print(" --- Menu Principal --- ")
    print("1. Numeros")
    print("2. Personas")
    print("3. Finalizar")
    op=int(input("Digite opcion 1-2-3: "))
    if op==1:
        Numeros() #invocamos a un def
    if op==2:
        Personas() #invocamos a un def
    if op==3:
        print("Programa finalizado")
        seguir=False
        break