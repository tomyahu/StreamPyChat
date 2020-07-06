import pygame
from consts import font_dir

def loadFont(font_name, font_size):
    return pygame.font.Font(font_dir + font_name, font_size)

defaultFont = loadFont('HUM521B.TTF', 20)
pokmn_em_font = loadFont('pkmnem.ttf', 30)
runemaster_font = loadFont('PIXEAB__.TTF', 16)