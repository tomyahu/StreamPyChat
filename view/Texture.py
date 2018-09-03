import pygame

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
        self.top = pygame.image.load('view/images/' + folder + '/top.png')
        self.top = pygame.transform.scale(self.top, (int(width), self.top.get_rect().size[1]))
        self.bottom = pygame.image.load('view/images/' + folder + '/bottom.png')
        self.bottom = pygame.transform.scale(self.bottom, (int(width), self.bottom.get_rect().size[1]))
        self.border = pygame.image.load('view/images/' + folder + '/border.png')
        self.border = pygame.transform.scale(self.border, (self.border.get_rect().size[0], int(height)))
        Texture.__init__(self, pygame.image.load('view/images/' + folder + '/background.png'), width, height)

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