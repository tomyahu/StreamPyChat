import pygame
from consts import winWidth, image_dir

def load_top_image(folder):
    return pygame.image.load(image_dir + folder + '/top.png')

def load_bottom_image(folder):
    return pygame.image.load(image_dir + folder + '/bottom.png')

def load_border_image(folder):
    return pygame.image.load(image_dir + folder + '/border.png')

def load_background_image(folder):
    return pygame.image.load(image_dir + folder + '/background.png')