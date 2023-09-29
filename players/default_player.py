import board
import numpy as np
import players.player as player


class DefaultPlayer(player.Player):

    def __init__(self, color:int, board:board.Board):
        super().__init__(color, board)
    
    def move(self, board:board.Board, debug:bool = False):
        """Randomly select a valid move"""
        # checks if it is the player's turn
        if board.turn != self.color:
            return
        
        valid_moves = board.get_allowed_moves()
        if len(valid_moves) == 0:
            return 0
        else:
            pass
            
    


