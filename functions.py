import os
import sys
from pyfiglet import figlet_format as banner


def clear():
    cmd = "clear"
    if "win" in sys.platform:
        cmd = "cls"
    os.system(cmd)


def get_board():
    board = {}
    for letter in ["a", "b", "c"]:
        board[letter] = {}
        for number in ["1", "2", "3"]:
            board[letter][number] = "-"

    return board

def board_to_str(inp: dict):
    out = ""
    for letter in inp:
        for num in inp[letter]:
            out += inp[letter][num]

    return out

def str_to_board(inp: str):
    out = {}
    inp = list(inp)
    ind = 0
    for letter in ["a", "b", "c"]:
        out[letter] = {}
        for num in ["1", "2", "3"]:
            out[letter][num] = inp[ind]
            ind += 1

    return out

def dict_to_str(inp: dict):
    out = ""
    for obj in inp:
        out += f"{obj}/{inp[obj]}|"
    out = out[:-1]

    return out

def str_to_dict(inp: str):
    out = {}
    inp = inp.split("|")
    for obj in inp:
        out[obj.split("/")[0]] = obj.split("/")[1]

    return out

def print_board(board):
    print(banner(f"""         1  2  3
a {board["a"]["1"]} {board["a"]["2"]} {board["a"]["3"]}
b {board["b"]["1"]} {board["b"]["2"]} {board["b"]["3"]}
c {board["c"]["1"]} {board["c"]["2"]} {board["c"]["3"]}
"""))


if __name__ == "__main__":
    print_board(get_board())
