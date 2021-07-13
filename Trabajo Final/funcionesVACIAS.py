from principal import *
from configuracion import *
import random
import math


#Lee el archivo línea por línea, remueve el "\n" y la apppendea a salida
def lectura(archivo, salida):
    for linea in archivo.readlines():
        palabra=linea[:-1]
        salida.append(palabra)

#Guarda una posición random de la lista silabas y devuelve el elemento de esa posición
def nuevaPalabra(silabas):
    pos=random.randrange(len(silabas))
    return silabas[pos]

#Recorre la palabra y cuando el elemento sea distinto a "-", lo va concatenando a palabraSinGuion
def silabasTOpalabra(palabra):
    palabraSinGuion=""
    for letra in palabra:
        if letra!="-":
            palabraSinGuion=palabraSinGuion+letra
    return palabraSinGuion

#Opcional
def palabraTOsilaba(palabra):
    nueva=separador(palabra)
    return nueva
##def palabraTOsilaba(palabraUsuario,lemarioSilabas):
##    for palabra in lemarioSilabas:
##        if palabraUsuario==silabasTOpalabra(palabra):
##            return palabra

#El primer for recorre la palabra separada en silabas y va guardando la posición del elemento que sea "-". Cuando termine de recorrer
#la palabra, se quedará con la posición del último "-". En el segundo for, concatenará los elementos cuyas posiciones sean mayores a la
#guardada en la variable pos (que es donde se encuentra el último "-"). Y retorna la silaba.
def dameUltimaSilaba(enSilabas):
    pos=-1
    silaba=""
    for i in range(len(enSilabas)):
        if enSilabas[i]=="-":
            pos=i
    for i in range(len(enSilabas)):
        if i>pos:
            silaba=silaba+enSilabas[i]
    return silaba

#Recorre la palabra separada en silabas y mientras el elemento sea distinto de "-", lo va concatenando.
#Una vez que encuentre el primer "-" devuelve la silaba. Esta funcion tambien comtempla los casos en que la palabra este
#formada por una sola silaba
def damePrimeraSilaba(enSilabas):
    silaba=""
    i=0
    for letra in enSilabas:
        if letra!="-":
            silaba=silaba+letra
        else:
            return silaba
    return silaba

#Esta función controla por un lado, si la palabra que ingresó el usuario se encuentra dentro de la lista de palabras
#y por otro, si la la primera silaba de la palabra que ingresó el usuario coincide con la última sílaba de la palabra que tiró la máquina.
def esValida(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario):
        for palabra in listaPalabrasDiccionario:
            if palabra==palabraUsuario and damePrimeraSilaba(palabraUsuarioEnSilabas)==dameUltimaSilaba(palabraEnSilabas):
                return True
        return False

#Esta función devuelve la cantidad de puntos (en que caso de que sea correcta) que es el resultado de 2 elevado a la longitud de la última
#silaba que ingresó el usuario
def Puntos(palabraUsuario,lemarioSilabas):
    return 2**len(dameUltimaSilaba(palabraTOsilaba(palabraUsuario)))

#Si el usuario ingresó "desconfio", llama a la función desconfio. Si el usuario tenía razón, llama a la función acierto y devuelve los puntos
#Si el usuario estaba equivocado, llama a la funcion fallo y devuelve los puntos
#Para palabras distintas a desconfio, llama a la funcion esValida y si lo es, llama a la función acierto y devuelve el valor que retorna la función Puntos
#Si no es valida, llama a la funcion fallo y devuelve la longitud de la palabra que ingresó el usuario en negativo.
def procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario,lemarioSilabas):
        puntos=0
        if palabraUsuario=="desconfio":
            puntos=desconfio(palabraEnSilabas,lemarioSilabas)
            if puntos==10:
                acierto()
                return puntos
            else:
                fallo()
                return puntos
        else:
            if esValida(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario):
                acierto()
                return Puntos(palabraUsuario,lemarioSilabas)


            else:
                fallo()
                return -len(palabraUsuario)

#Esta función para la música de fondo, guarda el sonido de acierto en una variable y la reproduce. Luego vuelve a cargar la música de fondo y la reproduce
def acierto():
    pygame.mixer.music.stop()
    a=pygame.mixer.Sound("acierto.wav")
    a.play()
    pygame.mixer.music.load("fondo.mp3")
    pygame.mixer.music.play(60)

#Esta función para la música de fondo, guarda el sonido de error en una variable y la reproduce. Luego vuelve a cargar la música de fondo y la reproduce
def fallo():
    pygame.mixer.music.stop()
    a=pygame.mixer.Sound("fallo.wav")
    a.play()
    pygame.mixer.music.load("fondo.mp3")
    pygame.mixer.music.play(60)

#Recorre el lemario de palabras separadas en sílabas y si hay una palabra que su primera sílaba coincida con la última sílaba de la palabra que tiró
#la máquina, el jugar perdió la jugada y devuelve un -10. Si no hay palabra, el usuario estaba en lo correcto y gana(devuelve) 10 puntos.
def desconfio(palabraEnSilabas,lemarioSilabas):
    for palabra in lemarioSilabas:
        if dameUltimaSilaba(palabraEnSilabas)==damePrimeraSilaba(palabra):
            return -10
    return 10

#opcional
#Si el usuario ingresó "desconfio", llama a la función nuevaPalabra para que tire una nueva palabra random. Sino, busca una palabra que su primera
#sílaba coincida con la sílaba que se pasa como parámetro y devuelve la palabra. Sino encuentra, devuelve una nueva palabra random.
def buscarPalabraQueEmpieceCon(silaba,lemarioEnSilabas,palabraUsuario):
    if palabraUsuario=="desconfio":
        return nuevaPalabra(lemarioEnSilabas)
    else:
        for i in range(len(lemarioEnSilabas)):
            palabra=nuevaPalabra(lemarioEnSilabas)
            if damePrimeraSilaba(palabra)==silaba:
                return palabra
        return nuevaPalabra(lemarioEnSilabas)
