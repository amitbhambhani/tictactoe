import os

from termcolor import colored

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
        selection = input("Place an X!\n")
        correctChosen = False
        while correctChosen == False:
            correctChosen = choice(selection, layout, "X")
            if correctChosen == True and checkWin(layout, patterns) == True:
                os.system("clear")
                board(layout)
                print("X wins!")
                return True
    else:
        selection = input("Place an O!\n")
        correctChosen = False
        while correctChosen == False:
            correctChosen = choice(selection, layout, "O")
            if correctChosen == True and checkWin(layout, patterns) == True:
                os.system("clear")
                board(layout)
                print("O wins!")
                return True


def game():
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
