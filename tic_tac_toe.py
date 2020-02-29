import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

TIE = 0
PLAYER1_WIN = 1
MACHINE_WIN = 2


class TicTacToeGame():
    def __init__(self):
        self.board = [None] * 9
        self.turn = _PLAYER
        self.is_game_over = False
        self.winner = None

    def is_over(self):  # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)

   
        esP =_PLAYER_SYMBOL
        es =_MACHINE_SYMBOL
            
        ganador_esP = ((self.board[3] == esP and self.board[4] == esP and self.board[5]== esP) or
        (self.board[6] == esP and self.board[7] == esP and self.board[8]== esP) or
        (self.board[0] == esP and self.board[1] == esP and self.board[2]== esP) or
        (self.board[0] == esP and self.board[3] == esP and self.board[6]== esP) or
        (self.board[1] == esP and self.board[4] == esP and self.board[7]== esP) or
        (self.board[2] == esP and self.board[5] == esP and self.board[8]== esP) or
        (self.board[2] == esP and self.board[4] == esP and self.board[6]== esP) or
        (self.board[0] == esP and self.board[4] == esP and self.board[8]== esP))
         

        ganador_es = ((self.board[3] == es and self.board[4] == es and self.board[5]== es) or
        (self.board[6] == es and self.board[7] == es and self.board[8]== es) or
        (self.board[0] == es and self.board[1] == es and self.board[2]== es) or
        (self.board[0] == es and self.board[3] == es and self.board[6]== es) or
        (self.board[1] == es and self.board[4] == es and self.board[7]== es) or
        (self.board[2] == es and self.board[5] == es and self.board[8]== es) or
        (self.board[2] == es and self.board[4] == es and self.board[6]== es) or
        (self.board[0] == es and self.board[4] == es and self.board[8]== es))

      

        if(ganador_es == True and es == _MACHINE_SYMBOL):
            self.winner = MACHINE_WIN
            self.is_game_over = True
            return self.is_game_over
        if (ganador_esP == True and esP == _PLAYER_SYMBOL):
            self.winner = PLAYER1_WIN
            self.is_game_over = True 
            return self.is_game_over
        
        #else:
        #    self.winner = TIE
         #   self.is_game_over = True
          #  return self.is_game_over

  
       
      


    def play(self):
        if self.turn == _PLAYER:
            self.player_turn()
            self.turn = _MACHINE
        else:
            self.machine_turn()
            self.turn = _PLAYER

    def player_choose_cell(self):
        print("Input empty cell bewtween 0 and 8")

        player_cell = input().strip()
        match = re.search("\d", player_cell)

        if not match:
            print("Input is not a number, please try again")

            return self.player_choose_cell()

        player_cell = int(player_cell)

        if self.board[player_cell] is not None:
            print("Cell is already taken, try again")

            return self.player_choose_cell()

        return player_cell

    def player_turn(self):
        chosen_cell = self.player_choose_cell()
        self.board[chosen_cell] = _PLAYER_SYMBOL

    def machine_turn(self):  # TODO: Finish this function by making the machine choose a random cell (use random module)
        random_ended = False

        while not random_ended:
            i = random.randrange(0,8)
            if self.board[i] is None:
                self.board[i] = _MACHINE_SYMBOL
                random_ended = True

    def format_board(self):
        row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
        row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
        row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

        return "\n".join([row0, row1, row2])

    def print(self):
        print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
        print(self.format_board())
        print()

    def print_result(self):  # TODO: Finish this function in order to print the result based on the *winner*
        if self.winner == MACHINE_WIN:
            print("Machine Won")
        elif self.winner == PLAYER1_WIN:
            print("Player Won")
        else:
            print("Has been a Tie")
