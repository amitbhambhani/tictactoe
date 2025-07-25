import os

from termcolor import colored

import crawl as cr

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


def board(layout):
    print("+---+---+---+")
    print(
        f"| {colored(layout[1], "grey")} | {colored(layout[2], "grey")} | {colored(layout[3], "grey")} |"
    )
    print("+---+---+---+")
    print(
        f"| {colored(layout[4], "grey")} | {colored(layout[5], "grey")} | {colored(layout[6], "grey")} |"
    )
    print("+---+---+---+")
    print(
        f"| {colored(layout[7], "grey")} | {colored(layout[8], "grey")} | {colored(layout[9], "grey")} |"
    )
    print("+---+---+---+")
    return None


def choice(choice, layout, turn):
    if not choice.isnumeric():
        print("Invalid choice, try again")
        return False
    num = int(choice)
    if num > 0 and num < 10 and layout[num] == str(num):
        if turn == "X":
            layout[num] = colored("X", (230, 69, 83))
        elif turn == "O":
            layout[num] = colored("O", (4, 165, 229))
        return True
    else:
        print("Invalid choice, try again")
        return False


def checkWin(layout, patterns):
    xPattern = ""
    oPattern = ""
    for key in layout:
        if layout[key] == colored("X", (230, 69, 83)):
            xPattern += f"{key}"
        if layout[key] == colored("O", (4, 165, 229)):
            oPattern += f"{key}"
    if xPattern in patterns or oPattern in patterns:
        return True
    return False


def placeMark(layout, patterns, turn):
    if turn % 2 == 0:
        correctChosen = False
        while correctChosen == False:
            selection = input("Place an X!\n")
            correctChosen = choice(selection, layout, "X")
            if correctChosen == True and checkWin(layout, patterns) == True:
                os.system("clear")
                board(layout)
                print("X wins!")
                return True
    else:
        correctChosen = False
        while correctChosen == False:
            selection = input("Place an O!\n")
            correctChosen = choice(selection, layout, "O")
            if correctChosen == True and checkWin(layout, patterns) == True:
                os.system("clear")
                board(layout)
                print("O wins!")
                return True


def intro():
    os.system("clear")
    cr.writer("Welcome to TicTacToe!")
    cr.writer("Just a couple reminders:")
    cr.writer("    - X goes first")
    cr.writer("    - You need 3 in a row to win")
    cr.writer("Good luck!")


def game():
    runIntro = False
    if runIntro:
        intro()

    turn = 0

    patterns = {"123", "456", "789", "159", "258", "357", "147", "369"}

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

    while True:
        board(layout)
        if turn == 9:
            print("Draw")
            break
        win = placeMark(layout, patterns, turn)
        if win == True:
            break
        turn += 1
        os.system("clear")


game()
