import pygame

class Texture():

    def __init__(self, image, width, height):
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.ancho = width
        self.alto = height

    def rescale_y(self, height):
        self.alto = height
        self.image = pygame.transform.scale(self.image, (int(self.ancho), int(height)))

    def get_texture(self):
        return Texture(self.image, self.ancho, self.alto)
