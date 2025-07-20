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
    if num > 0 and num < 10:
        layout[num] = turn
        return True
    else:
        print("Invalid choice, try again")
        return False


def checkWin(layout, patterns):
    xPattern = ""
    oPattern = ""
    for key in layout:
        if layout[key] == "X":
            xPattern += f"{key}"
        if layout[key] == "O":
            oPattern += f"{key}"
    if xPattern in patterns or oPattern in patterns:
        return True
    return False


def placeMark(layout, patterns, turn):
    pass


def game():
    pass
