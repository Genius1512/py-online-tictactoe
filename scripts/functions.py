# These are functions that are used by the server and the client. They handle
# the conversion from dictionnarys to strings, so the networking server can convert it into bytes, and
# the conversion from strings to the board.

import os
import sys
from pyfiglet import figlet_format as banner

# clear the console
def clear():
    cmd = "clear"
    if "win" in sys.platform:
        cmd = "cls"
    os.system(cmd)
    
# get board
def get_board():
    board = {}
    for letter in ["a", "b", "c"]:
        board[letter] = {}
        for number in ["1", "2", "3"]:
            board[letter][number] = "-"

    return board

# prints out the board
def print_board(board):
    print(banner(f"""         1  2  3
a {board["a"]["1"]} {board["a"]["2"]} {board["a"]["3"]}
b {board["b"]["1"]} {board["b"]["2"]} {board["b"]["3"]}
c {board["c"]["1"]} {board["c"]["2"]} {board["c"]["3"]}
"""))
