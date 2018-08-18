

class Msg():

    #recibe la posicion, la lista de texturas que representa
    #la animacion del boton y la pantalla
    def __init__(self, user, text):
        self.user = user
        self.text = text

    def get_user(self):
        return self.user

    def get_text(self):
        return self.text

