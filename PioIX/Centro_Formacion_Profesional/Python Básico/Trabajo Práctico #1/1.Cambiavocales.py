"""Código de Federico Noodt Molins
        ► Ejercicio 1: Crear un programa que permita ingresar frases de manera tal que cada vocal que contenga la frase la
         cambie por una única vocal que eligió el usuario al comienzo del mismo. Ej: Vocal de reemplazo: “a”, frase
         ingresada: “el silencio de otros”, resultado en pantalla: “al salancaa da atras”
        ► Punto extra incluido: En caso de que la vocal que va ser reemplazada tenga tilde, la “o” debera tenerlo también:
         Ej mamá ---> momó."""

vocalElegida = input("Ingrese una vocal: ").lower()[0]
frase = input("ingrese su frase: ")

#Comentario (1): El siguiente for es para encontrar la vocal acentuada.
vocalesAcentuadas = ["á", "é", "í", "ó", "ú"]
contador = 0
for extra in["a", "e", "i", "o", "u"]:
    if vocalElegida == extra:
        vElegidaAcentuada = vocalesAcentuadas[contador]
    contador = contador + 1

contador2 = 0

for j in ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]:
    if contador2 < 5:
        frase = frase.replace(j, vocalElegida)
    else:
        frase = frase.replace(j, vElegidaAcentuada)
    contador2 = contador2 + 1
print(frase)