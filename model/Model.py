from model.Msg import Msg
from model.User import User
from consts import messages_rendered


def get_msgs():
    file = open("RestreamChat.txt", "r")
    lineas = []
    linea_splited = file.readline().replace('\n', '').split(" ", 3)
    while linea_splited[0] != '':
        if len(linea_splited) == 4:
            lineas.append(linea_splited[3])
        linea_splited = file.readline().replace('\n', '').split(" ", 3)
    file.close()

    lineas = lineas[-20:][::-1]
    msgs = []

    for i in range(len(lineas)):
        linea_aux = lineas[i].split(": ", 1)
        if len(linea_aux) == 2:
            msgs.append(Msg(User(linea_aux[0]), linea_aux[1]))

    return msgs
