import socket

from termcolor import colored


def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 8001))

    while True:
        command = c.recv(1024).decode()

        if command == "Your turn":
            print("Make a move!")
            move = input("Pick a square")
            c.sendall(move.encode())
        elif command == "Their turn":
            print("Opponent is thinking...")
        elif command == "Done X" or command == "Done O":
            winner = len(command) - 1
            print(f"Game over! {command[winner]} wins!")
            break


client()
