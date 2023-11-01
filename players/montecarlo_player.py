from gameboard import Board
import numpy as np
from players.base_player import BasePlayer
from game import Game
from players.random_player import RandomPlayer

class MonteCarloPlayer(BasePlayer):
    def __init__(self, color:int, board:Board):
        super().__init__(color, board)
        self.game_board = board
        self.N_attempts = 10
        
    
    def move(self, board:Board, debug:bool = False):
        """Randomly select a valid move"""
        # checks if it is the player's turn

        if board.turn != self.color:
            return -1
        
        allowed_moves = board.get_allowed_moves()
        if len(allowed_moves) == 0:
            return 0
        
        scores = np.zeros(len(allowed_moves))

        for i, (x,y) in enumerate(allowed_moves):
            for _ in range(self.N_attempts):
                # create a game
                sim_board = Board()
                sim_board.state = board.state.copy()
                sim_board.play(x,y)
                # It should be the other player's turn
                sim_game = Game(RandomPlayer(-1, sim_board), 
                                RandomPlayer(1, sim_board), 
                                sim_board)
                w = sim_game.autoplay()
                if w == self.color:
                    scores[i] += 1
        
        if debug: 
            print(scores)
        
        best_move = allowed_moves[np.argmax(scores)]
        x, y = best_move
        return board.play(x, y)
            