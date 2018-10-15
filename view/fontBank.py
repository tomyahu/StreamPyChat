import pygame
from consts import font_dir

def loadFont(font_name, font_size):
    return pygame.font.Font(font_dir + font_name, font_size)

defaultFont = loadFont('HUM521B.TTF', 20)