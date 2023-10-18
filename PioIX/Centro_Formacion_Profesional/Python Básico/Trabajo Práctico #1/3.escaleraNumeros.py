"""Código de Federico Noodt Molins
        ► Ejercicio 3: Crear un programa que permita el ingreso de 10 números enteros. En caso de que haya 3 números
        consecutivos ascendentes(escalera), el sistema de volver a pedir nuevamente 10 números nuevos con un máximo de
        dos intentos más. En caso que llegue al máximo de intentos, mostrar un mensaje: “ Intentelo mañana otra vez”.
         Si logra ingresar los 10 números no consecutivos debe mostrarlo por pantalla y terminar el programa.
	Caso Feliz: 3-6-9-5-2-6-11-25-7-0
	Caso No Feliz: 3-5-6-7-8-2-3-99-1-3
        ► Punto extra incluido: Agregar la restricción consecutivos descendentes: Caso NO feliz: 6-2-3-9-8-7-1-2-24-3 """

menosaMas = True
masaMenos = True
escalera = 0
while (menosaMas or masaMenos) and escalera < 3:
    numerosLista = []
    for x in range(0, 10):
        ingreso = ""
        while ingreso == "":
            ingreso = input("ingrese valores: ")
        numero = int(ingreso)
        numerosLista.append(numero)
    menosaMas = False
    masaMenos = False

    for x in range(0, 8):
        if (numerosLista[x] - numerosLista[x + 1] == -1) and (numerosLista[x + 1] - numerosLista[x + 2] == -1):
            menosaMas = True
            print("Ingresó numeros consecutivos. Vuelva a ingresar la lista...")
            print("Caso no feliz:", numerosLista)
        if (numerosLista[x] - numerosLista[x + 1] == 1) and (numerosLista[x + 1] - numerosLista[x + 2] == 1):
            masaMenos = True
            print("Ingresó numeros consecutivos. Vuelva a ingresar la lista...")
            print("Caso no feliz:", numerosLista)
    if (masaMenos or menosaMas) == True:
        escalera = escalera + 1



if escalera == 3:
        print("Lo siento, ya cerramos el local.")
        menosaMas = False
        masaMenos = False

else:
     print("Caso feliz:", numerosLista)


