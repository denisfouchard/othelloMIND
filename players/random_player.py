from gameboard import Board
import numpy as np
from players.base_player import BasePlayer


class RandomPlayer(BasePlayer):

    def __init__(self, color:int, board:Board):
        super().__init__(color, board)
    
    def move(self, board:Board, debug:bool = False):
        """Randomly select a valid move"""
        # checks if it is the player's turn
        if board.turn != self.color:
            return
        
        valid_moves = board.get_allowed_moves()
        if len(valid_moves) == 0:
            return 0
        else:
            x, y = valid_moves[np.random.randint(len(valid_moves))]
            return board.play(x, y)
    


