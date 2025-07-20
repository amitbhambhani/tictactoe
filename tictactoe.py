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


board(layout)


def choice(choice, layout, turn):
    pass


def checkWin(layout, patterns):
    pass


def placeMark(layout, patterns, turn):
    pass


def game():
    pass
