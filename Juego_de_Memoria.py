#!/usr/bin/env python3

#########################################################
## Desarrollado en el Area de Control de Procesos del	#
## Dpto de Electronica de la UAM Azcapotzalco			#
## 														#
#########################################################

import pygame,sys, random  #importamos los modulos necesarios
from pygame.locals import *

inicio = True 	#variable que marca el inicio de un nuevo juego
FPS = 30		#Frames per second a los que actualizamos la pantalla 
ESPACIO_ENTRE_BOTONES = 30  #espacio entre los botones en pantall
ANCHO_BOTON = 162	#ancho de los botones (eje x)
ALTO_BOTON = 106	#alto de los botones (eje y)
VELOCIDAD = 25		#velocidad inicial del juego
FLASHDELAY = 500	#espera entre animaciones del juego (en milisegundos)
FLASHSPEED = 500	#velocidad inicial de las animaciones en botones
ANCHO_PANTALLA = 800	#Resolucion establecida para la pantalla touch 7' de la Raspberry
ALTO_PANTALLA = 450

##COLORES
BRAQUA=(0,255,255) #Los colores se guardan en variables mediante tuplas RGB
AQUA=(0,155,155)
BRAZUL=(0,0,255)
AZUL=(0,0,155)
BRGRIS=(125,125,125)
GRIS=(55,55,55)
BRVERDE=(0,128,0)
VERDE=(0,58,0)
BRMARRON=(128,0,0)
MARRON=(68,0,0)
BRMORADO=(128,0,128)
MORADO=(58,0,28)
BRROJO=(255,0,0)
ROJO=(155,0,0)
BRTEAL=(0,128,128)
TEAL=(0,28,28)
BRAMARILLO=(255,255,0)
AMARILLO=(155,155,0)
NEGRO=(0,0,0)
BLANCO=(255,255,255)
NEGRO2=(15,15,15)
##

#Los botones son objetos rectangulos creados con pygame.Rect.

#BOTONES  					(POS X DE ESQUINA SUPERIOR)        		(POS Y DE ESQUINA SUPERIOR)
AQUARECT = pygame.Rect(ESPACIO_ENTRE_BOTONES					,ESPACIO_ENTRE_BOTONES					,ANCHO_BOTON,ALTO_BOTON)
AZULRECT = pygame.Rect(ESPACIO_ENTRE_BOTONES*2+ANCHO_BOTON		,ESPACIO_ENTRE_BOTONES					,ANCHO_BOTON,ALTO_BOTON)
GRISRECT = pygame.Rect(ESPACIO_ENTRE_BOTONES*3+ANCHO_BOTON*2	,ESPACIO_ENTRE_BOTONES					,ANCHO_BOTON,ALTO_BOTON)

VERDERECT  = pygame.Rect(ESPACIO_ENTRE_BOTONES					,ESPACIO_ENTRE_BOTONES*2+ALTO_BOTON		,ANCHO_BOTON,ALTO_BOTON)
MARRONRECT = pygame.Rect(ESPACIO_ENTRE_BOTONES*2+ANCHO_BOTON	,ESPACIO_ENTRE_BOTONES*2+ALTO_BOTON		,ANCHO_BOTON,ALTO_BOTON)
MORADORECT = pygame.Rect(ESPACIO_ENTRE_BOTONES*3+ANCHO_BOTON*2	,ESPACIO_ENTRE_BOTONES*2+ALTO_BOTON		,ANCHO_BOTON,ALTO_BOTON)

ROJORECT 	= pygame.Rect(ESPACIO_ENTRE_BOTONES					,ESPACIO_ENTRE_BOTONES*3+ALTO_BOTON*2	,ANCHO_BOTON,ALTO_BOTON)
TEALRECT 	= pygame.Rect(ESPACIO_ENTRE_BOTONES*2+ANCHO_BOTON	,ESPACIO_ENTRE_BOTONES*3+ALTO_BOTON*2	,ANCHO_BOTON,ALTO_BOTON)
AMARILLORECT  = pygame.Rect(ESPACIO_ENTRE_BOTONES*3+ANCHO_BOTON*2	,ESPACIO_ENTRE_BOTONES*3+ALTO_BOTON*2	,ANCHO_BOTON,ALTO_BOTON)

NEGRORECT = pygame.Rect(0,0,ANCHO_PANTALLA,ALTO_PANTALLA)

#main  ### seccion principal del codigo
if __name__=='__main__':
	#variables globales
	pygame.init()
	fpsClock = pygame.time.Clock()
	VENTANA= pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))  #Se despliega la pantalla en el objeto VENTANA
	pygame.display.set_caption("MEMORIA")  #Titulo de la ventana

#variables de juego nuevo
	pattern=[]  #lista donde se generara la secuencia aleatoria del juego
	puntaje_jugador = 0 
	cuenta_actual = 0 #cuenta del patron 
	espera_entrada = False  ##Variable que controla si se espera respuesta del usuario o no

#letra
	fontObj=pygame.font.Font('freesansbold.ttf',25)   #creamos objetos para los textos del juego, el score en pantalla 
	fontObj2=pygame.font.Font('freesansbold.ttf',50)  # y el score final

#lista de los botones com pos 0-9
	mainBoard  = (AQUARECT,AZULRECT,GRISRECT,VERDERECT,MARRONRECT,MORADORECT,ROJORECT,TEALRECT,AMARILLORECT) 
		#lista de los colores 
	mainColors = (AQUA,AZUL,GRIS,VERDE,MARRON,MORADO,ROJO,TEAL,AMARILLO) #objeto del tablero de juego

	def drawButtons(): #funcion que dibuja los botones en pantalla
		pygame.draw.rect(VENTANA, AQUA, AQUARECT)
		pygame.draw.rect(VENTANA, AZUL, AZULRECT)
		pygame.draw.rect(VENTANA, GRIS, GRISRECT)
		pygame.draw.rect(VENTANA, VERDE, VERDERECT)
		pygame.draw.rect(VENTANA, MARRON, MARRONRECT)
		pygame.draw.rect(VENTANA, MORADO, MORADORECT)
		pygame.draw.rect(VENTANA, ROJO, ROJORECT)
		pygame.draw.rect(VENTANA, TEAL, TEALRECT)
		pygame.draw.rect(VENTANA, AMARILLO, AMARILLORECT)

	def getButtonClicked(x,y): # esta funcion recibe dos coordenadas y revisa si hubo o no colision con algun boton
		if AQUARECT.collidepoint((x,y)):   #de ser asi devuelve la tupla del color 
			return AQUA
		elif AZULRECT.collidepoint((x,y)):
			return AZUL
		elif GRISRECT.collidepoint((x,y)):
			return GRIS
		elif VERDERECT.collidepoint((x,y)):
			return VERDE
		elif MARRONRECT.collidepoint((x,y)):
			return MARRON
		elif MORADORECT.collidepoint((x,y)):
			return MORADO
		elif ROJORECT.collidepoint((x,y)):
			return ROJO
		elif TEALRECT.collidepoint((x,y)):
			return TEAL
		elif AMARILLORECT.collidepoint((x,y)):
			return AMARILLO
		return None
    
	def terminate():  #funcion para salir del juego
		pygame.quit()
		sys.exit()

	def gameOver():  #se ejecuta cuando el usuario ingreso incorrecto el patron
		pygame.time.wait(350)
		bot_sig = pygame.image.load('images/bot_next.png') #carga de la imagen del boton siguiente
		juego_terminado = pygame.image.load('images/Juego_terminado.png') #carga de la imagen de juego terminado
		VENTANA.blit(juego_terminado,[0,0]) #dibujamos la imagen en pantalla
		boton_siguiente = pygame.transform.smoothscale(bot_sig,(70,70)) #redimensionamos el tam del boton
		boton_siguiente_rect = boton_siguiente.get_rect() #creamos un objeto rectangulo para el boton sig
		boton_siguiente_rect.center = (735,400) #colocamos en posicion el rectangulo objeto
		VENTANA.blit(boton_siguiente,boton_siguiente_rect) #dibujamos el boton sobre su rectangulo
		gOverText = fontObj2.render((str(puntaje_jugador)),True,ROJO) #creamos el texto del score
		gOverRect = gOverText.get_rect() #obtenemos su rectangulo
		gOverRect.center = (ANCHO_PANTALLA/2,ALTO_PANTALLA*2/3) #posicionamos el rectangulo
		VENTANA.blit(gOverText,gOverRect) #dibujamos el score
		pygame.display.update() #acualizamos la pantalla
		wait_for_pushnext(boton_siguiente_rect) 
		sobre_el_proyecto = pygame.image.load('images/Sobre_el_proyecto.png') ## cambio a ventana con informacion sobre el proyecto
		VENTANA.blit(sobre_el_proyecto,[0,0])
		VENTANA.blit(boton_siguiente,boton_siguiente_rect)
		pygame.display.update()
		wait_for_pushnext(boton_siguiente_rect)

	def wait_for_pushnext(boton_siguiente_rect): ##Esta funcion recibe un objeto rectangulo y espera hasta que 
		espera=True								 ## el usuario lo presione para avanzar
		while espera:
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): 
					terminate()
				else:
					pygame.display.update()
				if event.type == MOUSEBUTTONUP:
					mousex,mousey = event.pos
					if boton_siguiente_rect.collidepoint((mousex,mousey)):
						espera = False

	def gameStart():  ##se ejecuta todas las veces que inicia o se reinicia el juego
		presentacion = pygame.image.load('images/Presentacion.png') #cargamos pantalla de presentacion
		instrucciones = pygame.image.load('images/Instrucciones.png') ## "" "" de instrucciones
		VENTANA.blit(presentacion,[0,0])
		bot_sig = pygame.image.load('images/bot_next.png')
		boton_siguiente = pygame.transform.smoothscale(bot_sig,(70,70))
		boton_siguiente_rect = boton_siguiente.get_rect()
		boton_siguiente_rect.center = (735,400)
		VENTANA.blit(boton_siguiente,boton_siguiente_rect)
		pygame.display.update()
		
		wait_for_pushnext(boton_siguiente_rect) #tras salir se cambia la pantalla de instrucciones

		VENTANA.blit(instrucciones,[0,0])
		VENTANA.blit(boton_siguiente,boton_siguiente_rect)
		pygame.display.update()

		wait_for_pushnext(boton_siguiente_rect)

	def flashButtonAnimation(color): #funcion que realiza el brillo de los botones cambiando los valores RGB
		if color == AQUA:
			flashColor = BRAQUA
			rectangle = AQUARECT
		elif color == AZUL:
			flashColor = BRAZUL
			rectangle = AZULRECT
		elif color == GRIS:
			flashColor = BRGRIS
			rectangle = GRISRECT
		elif color == VERDE:
			flashColor = BRVERDE
			rectangle = VERDERECT
		elif color == MARRON:
			flashColor = BRMARRON
			rectangle = MARRONRECT	
		elif color == MORADO:
			flashColor = BRMORADO
			rectangle = MORADORECT	
		elif color == ROJO:
			flashColor = BRROJO
			rectangle = ROJORECT	
		elif color == TEAL:
			flashColor = BRTEAL
			rectangle = TEALRECT	
		elif color == AMARILLO:
			flashColor = BRAMARILLO
			rectangle = AMARILLORECT

		origSurf = VENTANA.copy() #se guarda la superficie original
		flashSurf = pygame.Surface((ANCHO_BOTON,ALTO_BOTON))
		flashSurf = flashSurf.convert_alpha()
		r, g, b = flashColor
		for start,end, step in ((0,255,1),(255,0,-1)): #se aumenta y disminuye el brillo
			for alpha in range(start, end, VELOCIDAD*step):
				VENTANA.blit(origSurf,(0,0))
				flashSurf.fill((r, g, b, alpha))
				VENTANA.blit(flashSurf,rectangle.topleft)
				pygame.display.update()
				fpsClock.tick(FPS)
		VENTANA.blit(origSurf,(0,0))

	while True: #ciclo principal del juego
		clickedButton = None
		if inicio: #valores iniciales durante la primera ronda del juego
			gameStart()
			VELOCIDAD = 25
			FLASHDELAY = 500

		VENTANA.fill(NEGRO)
		drawButtons()
		st_button = pygame.image.load('images/start_button.png') #carga y colocacion del boton start
		start_button = pygame.transform.smoothscale(st_button,(164,64))
		start_button_rect = start_button.get_rect()
		start_button_rect.center = (690,350)
		VENTANA.blit(start_button,start_button_rect)
        
        #se crea y coloca el texto del Score
		scoreText = fontObj.render(('Puntaje: '+ str(puntaje_jugador)),True,BRROJO)
		scoreRect = scoreText.get_rect()
		scoreRect.center = (ESPACIO_ENTRE_BOTONES*4+ANCHO_BOTON*3+70,ANCHO_BOTON/2)
		VENTANA.blit(scoreText,scoreRect)
		
		for event in pygame.event.get(): #event handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): #si se pulsa esc o se da click en la X
				terminate()																#el juego se cierra
			elif event.type == MOUSEBUTTONUP:
				mousex,mousey = event.pos
				clickedButton = getButtonClicked(mousex,mousey)

		if inicio: #si es el primer patron espera a ejecutarlo hasta que el usuario pulse start
			wait_for_pushnext(start_button_rect)
			inicio = False

		if not espera_entrada:  ##ejecutar patron
			VELOCIDAD+=3
			FLASHDELAY-=15
			pygame.display.update()
			pygame.time.wait(1000)
			pattern.append(random.choice(mainColors))
			for button in pattern:
				flashButtonAnimation(button)
				pygame.time.wait(FLASHDELAY)
			espera_entrada=True
		else: ##espera a respuesta del usuario
			if clickedButton and clickedButton == pattern[cuenta_actual]:
				flashButtonAnimation(clickedButton)
				cuenta_actual+=1

				if cuenta_actual == len(pattern): #si termina correctamente el patron
					puntaje_jugador+=1
					espera_entrada = False
					cuenta_actual = 0

			elif(clickedButton and clickedButton != pattern[cuenta_actual]):
				#si se equivoca
				gameOver()
				pattern = []
				cuenta_actual = 0
				espera_entrada = False
				puntaje_jugador = 0
				inicio = True

		pygame.display.update()
		fpsClock.tick(FPS)
