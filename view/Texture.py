import pygame
from view.imageBank import load_background_image, load_border_image, load_bottom_image, load_top_image

class Texture():

    def __init__(self, image, width, height):
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.rescale(width, height)

    def rescale(self, width, height):
        self.ancho = width
        self.alto = height

    def rescale_y(self, height):
        self.alto = height
        self.image = pygame.transform.scale(self.image, (int(self.ancho), int(height)))

    def get_texture(self):
        return Texture(self.image, self.ancho, self.alto)

    def draw(self, screen,  xin, yin, xfin, yfin):
        screen.blit(self.image, (xin, yin))

class Spitted_Texture(Texture):

    def __init__(self, folder, width, height):
        self.folder = folder
        self.top = load_top_image(folder)
        self.top = pygame.transform.scale(self.top, (int(width), self.top.get_rect().size[1]))
        self.bottom = load_bottom_image(folder)
        self.bottom = pygame.transform.scale(self.bottom, (int(width), self.bottom.get_rect().size[1]))
        self.border = load_border_image(folder)
        self.border = pygame.transform.scale(self.border, (self.border.get_rect().size[0], int(height)))
        Texture.__init__(self, load_background_image(folder), width, height)

    def rescale_y(self, height):
        Texture.rescale_y(self, height)
        self.border = self.border = pygame.transform.scale(self.border, (self.border.get_rect().size[0], int(height)))

    def draw(self, screen, xin, yin, xfin, yfin):
        Texture.draw(self,screen,xin,yin, xfin, yfin)
        screen.blit(self.top, (xin, yin))
        screen.blit(self.bottom, (xin, yfin - self.bottom.get_rect().size[1]))
        screen.blit(self.border, (xin, yin))
        screen.blit(self.border, (xfin, yin))

    def get_texture(self):
        return Spitted_Texture(self.folder, self.ancho, self.alto)