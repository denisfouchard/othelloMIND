import board
import numpy as np
import players.player as player

class GreedyPlayer(player.Player):
    def __init__(self, color:int, board:board.Board):
        super().__init__(color, board)
        self.wmap = np.ones((8, 8))

        # Add weights to the four edges
        self.wmap[0, :] += 1
        self.wmap[7, :] += 1
        self.wmap[:, 0] += 1
        self.wmap[:, 7] += 1

        # Add weights to the four corners
        self.wmap[0, 0] += 3
        self.wmap[0, 7] += 3
        self.wmap[7, 0] += 3
        self.wmap[7, 7] += 3
    
    def move(self, board:board.Board):
        """Randomly select a valid move"""
        # checks if it is the player's turn
        if board.turn != self.color:
            return -1
        
        best_move = board.eval_game(self.wmap)
        if best_move != None:
            x, y = best_move
            return board.play(x, y)
        else:
            return -1