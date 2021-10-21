from networking import Server
from functions import *
import time as t


class App:
    def __init__(self):
        self.server = Server()
        self.server.setup()

        self.server.new_connection("p1")
        self.server.post(["p1"], "x")
        t.sleep(0.2) # I really dont now why this is required, but it does not work without it

        self.server.new_connection("p2")
        self.server.post(["p2"], "o")
        t.sleep(0.2) # I really dont now why this is required, but it does not work without it

        self.board = get_board()

        self.done = False
        while not self.done:
            self.get_turn("p1")
            state = self.test_state(self.board)
            if not state == None:
                self.server.post(["p1", "p2"], dict_to_str({
                    "reason": "end",
                    "content": f"{state};{board_to_str(self.board)}"
                }))
                quit()

            self.get_turn("p2")
            state = self.test_state(self.board)
            if not state == None:
                self.server.post(["p1", "p2"], dict_to_str({
                    "reason": "end",
                    "content": state
                }))
                quit()

    def get_turn(self, id):
        self.server.post([id], dict_to_str({
            "reason": "your-turn",
            "content": board_to_str(self.board)
        }))

        self.board = str_to_board(self.server.get(id))

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
