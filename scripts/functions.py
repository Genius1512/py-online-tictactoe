# These are functions that are used by the server and the client. They handle
# the conversion from dictionnarys to strings, so the networking server can convert it into bytes, and
# the conversion from strings to the board.

import os
import sys
from rich import print

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
    banner = """
  -------------
a | 1 | 2 | 3 |
  -------------
b | 4 | 5 | 6 |
  -------------
c | 7 | 8 | 9 |
  -------------
"""
    ind = 0
    for letter in board:
        for num in board[letter]:
            ind += 1
            banner = banner.replace(str(ind), board[letter][num]
                                              .replace("-", " ")
                                              .replace("x", "[red]x[/red]")
                                              .replace("o", "[blue]o[/blue]"))
    banner = "    1   2   3" + banner # numbers at the top would get replaced too
    
    print(f"[white]{banner}")
