import board
import numpy as np
import players.player as player


class RandomPlayer(player.Player):

    def __init__(self, color:int, board:board.Board):
        super().__init__(color, board)
    
    def move(self, board:board.Board):
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
    


