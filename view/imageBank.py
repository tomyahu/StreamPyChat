import pygame
from view.Texture import Texture
from consts import winWidth, image_dir

marcoTex = Texture(pygame.image.load(image_dir + 'MarcoMSG1.png'), winWidth*0.95, 100)

def load_top_image(folder):
    return pygame.image.load(image_dir + folder + '/top.png')

def load_bottom_image(folder):
    return pygame.image.load(image_dir + folder + '/bottom.png')

def load_border_image(folder):
    return pygame.image.load(image_dir + folder + '/border.png')

def load_background_image(folder):
    return pygame.image.load(image_dir + folder + '/background.png')