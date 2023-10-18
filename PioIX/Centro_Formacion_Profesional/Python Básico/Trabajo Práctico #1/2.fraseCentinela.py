"""Código de Federico Noodt Molins
        ► Ejercicio 2: Crear un programa que pida al usuario cargar una frase que finalice con “*” y a la frase resultante
         separarla en dos listas, una  de vocales y la otra de las consonantes según su orden de aparición. Mostrando
         cada letra por cada una de las listas. EJ: frase ingresada: “el pajaro canta hasta morir*” ,lista de vocales:
          e-a-a-o-a-a-a-a-o-i, lista de consonantes:l-p-j-r-c-t-h-s-t-m-r-r
        ► Punto extra incluido: Reporte extra de cuantas vocales hay por cada vocal. Para nuestro ejemplo. a=6, e=1, i=1, 0=2, u=0. """

print("Ingrese una frase (* para finalizar):")

fraseDivisora = input("►     ")
contador = 0
correcto = True
while fraseDivisora[len(fraseDivisora) - 1] != "*" and contador < 5:

    print("Ingrese una frase, y al finalizar coloque * ")
    fraseDivisora = input("►     ")
    if contador < 4:
        correcto = True
    else:
        correcto = False
    contador = contador + 1
if not correcto:
    print(" ☻ Excedió el numero de intentos.- ☻ ")
else:
    vocales = []
    consonantes = []

    for j in range(0, len(fraseDivisora) - 1):
        if fraseDivisora[j] == "a" or fraseDivisora[j] ==  "e" or fraseDivisora[j] ==  "i" or fraseDivisora[j] ==  "o" or fraseDivisora[j] ==  "u" or fraseDivisora[j] ==   "á" or fraseDivisora[j] ==  "é" or fraseDivisora[j] ==  "í" or fraseDivisora[j] ==  "ó" or fraseDivisora[j] ==  "ú":
            vocales.append(fraseDivisora[j])
        elif fraseDivisora[j] != " ":
            consonantes.append(fraseDivisora[j])
    print("Vocales:", vocales, "♦", "Consonantes:", consonantes)
    print("   ")
    print("Cantidad de vocales:", len(vocales), "♦", "cantidad de consonantes:", len(consonantes))
    print("   ")
    listadeVocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    contador2 = 0
    for j in listadeVocales:
        print(listadeVocales[contador2], "=", vocales.count(j))
        contador2 = contador2 + 1