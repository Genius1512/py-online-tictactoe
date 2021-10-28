# This is the server for tictactoe. It handles the communication 
# between the two clients

from networking import Server
from functions import *
import time as t
from rich import print


class App:
    def __init__(self, port):
        # setup server
        self.server = Server()
        self.server.setup(port=port, listen_to=5)
        # get connections
        for id in [("p1", "x"), ("p2", "o")]:
            self.server.new_connection(id[0])
            self.server.post([id[0]], id[1])
            t.sleep(0.2)

        print("")

        self.board = get_board() # init game board

        self.done = False
        while not self.done:
            for id in ["p1", "p2"]:
                print(f"[white][blue]{id.upper()}[/blue]'s turn")
                self.get_turn(id)
                print(f"[white][blue]{id.upper()}[/blue] made their turn\n")
                state = self.test_state(self.board)
                if not state == None: # ending
                    self.server.post(["p1", "p2"], {
                        "reason": "end",
                        "state": state,
                        "board": self.board
                    })
                    raise End()

    def get_turn(self, id):
        self.server.post([id], {
            "reason": "your-turn",
            "board": self.board
        })

        self.board = self.server.get(id)

    def test_state(self, board):
        # horizontal
        for letter in board:
            x_in_row = 0
            o_in_row = 0
            for num in board[letter]:
                if board[letter][num] == "x":
                    x_in_row += 1
                elif board[letter][num] == "o":
                        o_in_row += 1
            if x_in_row == 3:
                return "x"
            elif o_in_row == 3:
                return "o"
        # vertical
        for num in ["1", "2", "3"]:
            x_in_row = 0
            o_in_row = 0
            for letter in board:
                if board[letter][num] == "x":
                    x_in_row += 1
                elif board[letter][num] == "o":
                        o_in_row += 1
            if x_in_row == 3:
                return "x"
            elif o_in_row == 3:
                return "o"
        # diagonal
        if f'{board["a"]["1"]}{board["b"]["2"]}{board["c"]["3"]}' == "xxx":
            return "x"
        if f'{board["a"]["1"]}{board["b"]["2"]}{board["c"]["3"]}' == "ooo":
            return "o"
        if f'{board["a"]["3"]}{board["b"]["2"]}{board["c"]["1"]}' == "xxx":
            return "x"
        if f'{board["a"]["3"]}{board["b"]["2"]}{board["c"]["1"]}' == "ooo":
            return "o"
        # tie
        is_tie = True
        for letter in board:
            for num in board[letter]:
                if board[letter][num] == "-":
                    is_tie = False
                    break
        if is_tie:
            return "tie"


if __name__ == "__main__":
    app = App()
