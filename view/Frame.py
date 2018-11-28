import pygame
from consts import winWidth, winHeight
from view.textureBank import marcoTex
from view.fontBank import defaultFont
from view.textureBank import defaultTex

class Frame():

    #recibe la posicion, la lista de texturas que representa
    #la animacion del boton y la pantalla
    def __init__(self, msg, texture, screen, messages_below_y, font):
        self.msg = msg
        self.font = font
        self.tex = texture.get_texture()
        self.screen = screen
        self.x = winWidth/2
        self.y = messages_below_y - self.tex.alto/2

    #dbuja el boton
    def draw(self):
        self.y += self.tex.alto/2
        self.tex.rescale_y(self.font.size("a")[1] * self.get_lines_msg() + 20)
        self.y -= self.tex.alto / 2
        self.tex.draw(self.screen, self.getXin(), self.getYin(), self.getXfin(), self.getYfin())
        self.drawText((255,255,255))

    def get_lines_msg(self):
        text = self.msg.user.name + ': ' + self.msg.get_text()
        rect = pygame.Rect(self.getXin() + 10, self.getYin() + 10, self.tex.ancho - 20, winHeight / 4)
        font = self.font

        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        lines = 0
        while text:
            i = 1
            lines += 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return lines

    def drawText(self, color, aa=False, bkg=None):
        text = self.msg.user.name + ': ' + self.msg.get_text()
        surface = self.screen
        rect = pygame.Rect(self.getXin()+10, self.getYin()+10, self.tex.ancho-20, winHeight/4)
        font = self.font

        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        lines = 0
        while text:
            i = 1
            lines += 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text

    #se destruye el objetp
    def kill(self):
        del self

    # devuelve el x mas a la izquierda de su textura
    def getXin(self):
        return self.x - (self.tex.ancho/2)

    # devuelve el y mas arriba de su textura
    def getYin(self):
        return self.y - (self.tex.alto/2)

    # devuelve el x mas a la derecha de su textura
    def getXfin(self):
        return self.x + (self.tex.ancho/2)

    # devuelve el y mas abajo de su textura
    def getYfin(self):
        return self.y + (self.tex.alto/2)

class FrameFactory():

    def __init__(self):
        self.texture = defaultTex
        self.font = defaultFont

    def set_texture(self, tex):
        self.texture = tex

    def set_font(self, font):
        self.font = font

    def get_Frame(self, msg, screen, messages_below):
        return Frame(msg, self.texture, screen, messages_below, self.font)



class DefaultFrame(Frame):

    def __init__(self, msg, screen, messages_below):
        Frame.__init__(self, msg, marcoTex, screen, messages_below, defaultFont)

