import os
import pygame
from pygame.locals import *
from consts import winHeight, winWidth, FPS, COLOR_Black
from model.Model import get_msgs

# Se inician modulos
pygame.init()
pygame.font.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

from view.Frame import DefaultFrame, FrameFactory
from view.textureBank import *
from view.fontBank import *


# Se inicia la pantalla
surface = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Chat')

# Se crea el reloj
clock = pygame.time.Clock()

# Se crea la fabrica de frames
factory = FrameFactory()
factory.set_font(runemaster_font)
factory.set_texture(runemaster_tex)

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
    y_separation = 10
    for i in range(len(msgs)):
        curr_frame = factory.get_Frame(msgs[i], surface, winHeight - total_y)
        curr_frame.draw()
        total_y += curr_frame.tex.alto + y_separation



    # Vuelca lo dibujado en pantalla
    pygame.display.flip()
