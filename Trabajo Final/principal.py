#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *

from funcionesVACIAS import *

#Funcion principal
def main():

       #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("El juego del Mago Goma...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #Carga la música del juego y la reproduce
        pygame.mixer.music.load("fondo.mp3")
        pygame.mixer.music.play(60)

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        puntos = 0
        palabraUsuario = ""
        lemarioEnSilabas=[]
        listaPalabrasDiccionario=[]

        archivo= open("lemario.txt","r")
        archivo2= open ("lemarioSilabas.txt","r")

        #lectura del diccionario
        lectura(archivo, listaPalabrasDiccionario)

        #lectura del archivo en silabas
        lectura(archivo2, lemarioEnSilabas)

        #elige una al azar
        palabraEnSilabas=nuevaPalabra(lemarioEnSilabas)
        palabraActual=silabasTOpalabra(palabraEnSilabas)

        dibujar(screen, palabraUsuario, palabraActual, puntos,segundos)
        pygame.display.set_caption("TP2018_2do_semestre")
        done=False
        clock=pygame.time.Clock()
        background_image=pygame.image.load("inicio.png").convert()


        screen.blit(background_image,(0,0))
        pygame.display.flip()
        clock.tick(30)


        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()


            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #pasa la palabra a silabas
                        palabraUsuarioEnSilabas=palabraTOsilaba(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        puntos += procesar(palabraUsuario, palabraUsuarioEnSilabas,palabraActual, palabraEnSilabas, listaPalabrasDiccionario,lemarioEnSilabas)

                        #busca la ultima silaba y busca una palabra que empiece asi
                        silaba=dameUltimaSilaba(palabraUsuarioEnSilabas)
                        palabraEnSilabas=buscarPalabraQueEmpieceCon(silaba,lemarioEnSilabas,palabraUsuario)
                        palabraActual=silabasTOpalabra(palabraEnSilabas)
                        palabraUsuario = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, palabraActual,puntos,segundos)

            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

        archivo.close()
        archivo2.close()

        reloj1.tick(20)
        pantalla.blit(imagenfondo,(0,0))
        pygame.display.update()

        pygame.quit()

        pygame.init()
        size=[700,500]
        screen=pygame.display.set_mode(size)

        while done==False:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    done=True

        screen.blit(background_image,(0,0))
        pygame.display.flip()
        clock.tick(20)

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()


