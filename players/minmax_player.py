from gameboard import Board
from players.base_player import BasePlayer
from players.utils import minmax_heuristic


class MinMaxPlayer(BasePlayer):

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
        
        best_move, _ = minmax_move(board, valid_moves, self.color, minmax_heuristic)

        if best_move is None:
            if debug: print("MinMaxPlayer has no possible moves left.")
            return 
        
        x, y = best_move

        return board.play(x, y)
        



def minmax_move(board:Board, valid_moves, _color, heuristic):

    if len(valid_moves) == 0:
        return None, 0

    if len(valid_moves) == 1:
        sim_board = Board()
        sim_board.state = board.state.copy()
        x, y = valid_moves[0]
        sim_board.play(x, y)
        score = heuristic(sim_board, _color)

        return (x, y), score
        
    
    best_move = valid_moves[0]
    opponent_best_score = 0
    opponent_color = - _color

    for x, y in valid_moves:
        sim_board = Board()
        sim_board.state = board.state.copy()
        sim_board.turn = int(board.turn)
        
        sim_board.play(x,y, no_check=True)
        oppenent_valid_moves = sim_board.get_allowed_moves()
        _, opponent_score = minmax_move(sim_board, 
                                        oppenent_valid_moves,
                                        _color= opponent_color, 
                                        heuristic = heuristic
                                        )
        
        if opponent_score < opponent_best_score:
            opponent_best_score = opponent_score
            best_move = (x, y)
    
    x, y = best_move
    sim_board.play(x, y)

    best_score = heuristic(sim_board, _color)

    return best_move, best_score

