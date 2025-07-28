import socket
import threading

from tictactoe import checkWin, choice, intro, placeMark, stringBoard

clients = {}


def handleClient(conn, id):
    pass


def runGame():
    layout = {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }

    patterns = {"123", "456", "789", "159", "258", "357", "147", "369"}


def server(host, port):
    id = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(2)

    while id < 2:
        conn, addr = s.accept()
        clients[id] = conn
        threading.Thread(target=handleClient, args=(conn, id)).start()
        id += 1

    runGame()


# server()
