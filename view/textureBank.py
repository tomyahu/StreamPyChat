from consts import winWidth
from view.Texture import *

def create_splitted_texture(folder):
    return Spitted_Texture(folder, winWidth * 0.95, 100)

defaultTex = create_splitted_texture('default')