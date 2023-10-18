#====================================================CONSTANTES========================================================#

posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turnos = 0

triunfoX = False
triunfoCuadrado = False
empate = False

#===================================================DEFINICIONES=======================================================#

def jugador1():
    print('El jugador 1 usará X...')
    print('    ¿Como te llamas?')
    jugador1 = input('  ')
    return jugador1

def jugador2():
    print('Y el jugador 2 usará ■...')
    print('    ¿Cuál es su nombre?')
    jugador2 = input('  ')
    return jugador2

def bienvenida():
    print(" ______________________________")
    print("|          |         |         |                Bienvenido al...")
    print("|    ○     |    ○    |    ■    |                            TA")
    print("|__________|_________|_________|                                TE")
    print("|          |         |         |                                    TI")
    print("|    ■     |    ■    |    ○    |")
    print("|__________|_________|_________|")
    print("|          |         |         |")
    print("|    ○     |    ■    |    ■    |")
    print("|__________|_________|_________|                    ¿Comenzámos?")
    input("                                                        ")

def tabla():
    print("                                          ▼                ☼")
    print("                           ▼                            ☼")
    print("          ♦                     ▼                    ☼  ")
    print("             ♦  ________________________________  ☼")
    print("               |          |          |          |  ")
    print("               |    ", posiciones[0], "   |    ",posiciones[1] , "   |    ",posiciones[2] , "   |        ◄")
    print("       ►       |__________|__________|__________|    ◄")
    print("        ►      |          |          |          |  ")
    print("               |    ", posiciones[3], "   |    ", posiciones[4], "   |    ", posiciones[5], "   |  ")
    print("     ►         |__________|__________|__________|  ")
    print("       ►       |          |          |          | ◄")
    print("           ►   |    ", posiciones[6], "   |    ", posiciones[7], "   |    ", posiciones[8], "   |   ◄")
    print("         ►     |__________|__________|__________|        ◄")
    print("             ☼   ▲                               ♦")
    print("          ☼                     ▲                   ♦")
    print("       ☼             ▲                                 ♦              ")
    print("                         ▲                                ♦          ")
    print("                      ▲                                      ")


def agregarCirculo():
    circulo = int(input('Ingrese posición ○...     '))
    posiciones.remove(circulo)
    posiciones.insert(circulo-1, '○')
    return circulo

def agregarCuadrado():
    cuadrado = int(input('ingrese posición ■...     '))
    posiciones.remove(cuadrado)
    posiciones.insert(cuadrado-1, '■')
    return cuadrado

def incrementarTurno(turnos):
    turnos = turnos + 1
    return turnos

def victoriaCirculo(circulo):
    triunfoCirculo = False
    if circulo == 1 and circulo == 2 and circulo == 3 or circulo == 4 and circulo == 5 and circulo == 6 or circulo == 7 and circulo == 8 and circulo == 9:
        triunfoCirculo = True
        return triunfoCirculo



def victoriaCuadrado(cuadrado):
    triunfoCuadrado = False
    if cuadrado == 1 and cuadrado == 2 and cuadrado == 3 or cuadrado == 4 and cuadrado == 5 and cuadrado == 6 or cuadrado == 7 and cuadrado == 8 and cuadrado == 9:
        triunfoCuadrado = True
        return triunfoCuadrado



def resoluciondeEmpate():
    empate = False
    if turnos > 9 and triunfoX == False and triunfoCuadrado == False:
        empate = True
        return empate



def resultado():
    if triunfoX == True:
        print('¡Victoria! ¡Gano', jugador1)
    elif triunfoCuadrado == True:
        print('¡Victoria! ¡Gano', jugador2)
    elif empate == True:
        print('▓▓▓▓▓ E ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ T ▓▓▓▓▓▓▓▓▓▓▓▓')
        print('▓▓▓▓▓▓▓▓▓▓ M ▓▓▓▓▓▓▓▓▓▓ A ▓▓▓▓▓▓▓▓▓▓ E ▓▓▓▓')
        print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ P ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')

#==============================================CUERPO DEL PROGRAMA=====================================================#


#-----------Bienvenida al juego------------------------

bienvenida()

jugador1()
jugador2()

#-----------Juego--------------------------------------
tabla()

while triunfoX == False and triunfoCuadrado == False and empate == False:
    jugador1 = agregarCirculo()
    incrementarTurno(turnos)
    victoriaCirculo(circulo)
    tabla()

    jugador2 = agregarCuadrado()
    incrementarTurno(turnos)
    victoriaCuadrado()
    tabla()




#-----------Resolución----------------------------------

resultado()