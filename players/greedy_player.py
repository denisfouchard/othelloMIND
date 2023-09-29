import board
import numpy as np
import players.player as player
from players.utils import build_wmap

class GreedyPlayer(player.Player):
    def __init__(self, color:int, board:board.Board):
        super().__init__(color, board)
        self.wmap = build_wmap()
        
    
    def move(self, board:board.Board, debug:bool = False):
        """Randomly select a valid move"""
        # checks if it is the player's turn
        if board.turn != self.color:
            return -2
        
        best_move = board.eval_game(self.wmap)
        if debug: print(f"Best move is {best_move}")
        if best_move != None:
            x, y = best_move
            return board.play(x, y)
        else:
            return -1