import os
import pygame
from pygame.locals import *
from consts import winHeight, winWidth, FPS, COLOR_Black
from model.Model import get_msgs
from view.Frame import DefaultFrame

# Se inician modulos
pygame.init()
pygame.font.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Se inicia la pantalla
surface = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Chat')

# Se crea el reloj
clock = pygame.time.Clock()

# Entra en bucle principal
while True:

    # Setea el reloj
    clock.tick(FPS)

    # Busca eventos de aplicacion
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    #inicio del programa

    #Dibuja
    # Dibuja la pantalla
    surface.fill(COLOR_Black)

    msgs = get_msgs()
    frames = []

    total_y = 10
    for i in range(len(msgs)):
        curr_frame = DefaultFrame(msgs[i], surface, total_y)
        curr_frame.draw()
        total_y += curr_frame.tex.alto + 10



    # Vuelca lo dibujado en pantalla
    pygame.display.flip()