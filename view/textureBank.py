from consts import winWidth
from view.Texture import *
from consts import image_dir

def create_splitted_texture(folder):
    return Spitted_Texture(folder, winWidth * 0.95, 100)

defaultTex = create_splitted_texture('default')
runemaster_tex = create_splitted_texture('runemaster')
marcoTex = Texture(pygame.image.load(image_dir + 'MarcoMSG1.png'), winWidth*0.95, 100)