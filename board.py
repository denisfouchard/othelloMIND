import numpy as np
import matplotlib.pyplot as plt

class Board():
    """A class representing an Othello board.

    Attributes:
        state (numpy.ndarray): An 8x8 array representing the current state of the board.
        player1 (int): The number of pieces belonging to player 1 (white).
        player2 (int): The number of pieces belonging to player 2 (black).
        turn (int): The current turn, represented by -1 for player 1 and 1 for player 2.
        opponent (int): The opponent of the current player, represented by 1 for player 1 and -1 for player 2.
        black_pos (tuple): A tuple of arrays representing the positions of black pieces on the board.
        white_pos (tuple): A tuple of arrays representing the positions of white pieces on the board.

    Methods:
        adjacent_to_opponent(x, y): Returns True if the given position is adjacent to an opponent's piece.
        is_allowed_adj(x, y): Returns True if the given move is allowed according to Othello rules.
        get_black_white_positions(): Returns the positions of black and white pieces on the board.
        flip_pieces(x, y): Flips the pieces around the given move according to Othello rules.
        check_play(x, y, in_place=False): Checks if the given move is allowed and updates the board accordingly.
    """

    def __init__(self):
        """Initializes the Othello board with the starting configuration."""
        self.state = np.zeros((8,8), dtype=int)
        #white
        self.player1 = 32
        #black
        self.player2 = 32

        # start with white
        self.turn = -1
        self.opponent = 1

        # 0 is empty
        # 1 is white
        # 2 is black
        self.state[3,3] = -1
        self.state[4,4] = -1
        self.state[3,4] = 1
        self.state[4,3] = 1

        self.black_pos = np.where(self.state == 1)
        self.white_pos = np.where(self.state == -1)

    def adjacent_to_opponent(self, x:int, y:int) -> bool:
        """Returns True if the given position is adjacent to an opponent's piece."""
        # if the position is on the edge, avoid out of bounds error
        #check for every corner
        if x == 0 and y == 0:
            return self.state[x+1,y] == self.opponent or \
            self.state[x,y+1] == self.opponent or \
            self.state[x+1,y+1] == self.opponent
        if x == 7 and y == 0:
            return self.state[x-1,y] == self.opponent or \
            self.state[x,y+1] == self.opponent or \
            self.state[x-1,y+1] == self.opponent
        if x == 0 and y == 7:
            return self.state[x+1,y] == self.opponent or \
            self.state[x,y-1] == self.opponent or \
            self.state[x+1,y-1] == self.opponent
        if x == 7 and y == 7:
            return self.state[x-1,y] == self.opponent or \
            self.state[x,y-1] == self.opponent or \
            self.state[x-1,y-1] == self.opponent
        #check for every edge
        if x == 0:
            return self.state[x+1,y] == self.opponent or \
            self.state[x,y-1] == self.opponent or \
            self.state[x,y+1] == self.opponent or \
            self.state[x+1,y+1] == self.opponent or \
            self.state[x+1,y-1] == self.opponent
        if x == 7:
            return self.state[x-1,y] == self.opponent or \
            self.state[x,y-1] == self.opponent or \
            self.state[x,y+1] == self.opponent or \
            self.state[x-1,y-1] == self.opponent or \
            self.state[x-1,y+1] == self.opponent
        if y == 0:
            return self.state[x-1,y] == self.opponent or \
            self.state[x+1,y] == self.opponent or \
            self.state[x,y+1] == self.opponent or \
            self.state[x-1,y+1] == self.opponent or \
            self.state[x+1,y+1] == self.opponent
        if y == 7:
            return self.state[x-1,y] == self.opponent or \
            self.state[x+1,y] == self.opponent or \
            self.state[x,y-1] == self.opponent or \
            self.state[x-1,y-1] == self.opponent or \
            self.state[x+1,y-1] == self.opponent
        
        return self.state[x-1,y] == self.opponent or \
            self.state[x+1,y] == self.opponent or \
            self.state[x,y-1] == self.opponent or \
            self.state[x,y+1] == self.opponent or \
            self.state[x-1,y-1] == self.opponent or \
            self.state[x+1,y+1] == self.opponent or \
            self.state[x-1,y+1] == self.opponent or \
            self.state[x+1,y-1] == self.opponent
    
    def is_allowed_adj(self, x:int, y:int) -> bool:
        """Returns True if the given move is allowed according to Othello rules."""
        # check if move is allowed in othello rules
        # check if move is in bounds
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False
        # check if move is on empty square
        if self.state[x,y] != 0:
            return False
        # check if move is adjacent to opponent piece
        return self.adjacent_to_opponent(x,y)

    def get_black_white_positions(self) -> tuple:
        """Returns the positions of black and white pieces on the board."""
        self.black_pos = np.where(self.state == 1)
        self.white_pos = np.where(self.state == -1)
        return self.black_pos, self.white_pos
    
    def flip_pieces(self, x:int, y:int) -> None:
        """Flips the pieces around the given move according to Othello rules."""
        self.state[x,y] = self.turn
    
   

    def eval_move(self, x:int, y:int, wmap=np.ones((8,8)), in_place=False) -> int:
        """Checks if the given move is allowed and updates the board accordingly.

        Args:
            x (int): The x-coordinate of the move.
            y (int): The y-coordinate of the move.
            wmap (numpy.ndarray, optional): A 8x8 array representing the weight map of the board. Defaults to None.
            in_place (bool, optional): Whether to update the board in place. Defaults to False.

        Returns:
            int: The number of pieces flipped by the move.
        """
        # play move
        # check if move is allowed
        if not self.is_allowed_adj(x,y):
            return 0
        
        d=0

        next_state = self.state.copy()

        #flip pieces around the move like in othello rules
        # check if there is a line of opponent pieces in any direction and then a piece of the player
        # if so, flip all opponent pieces in that line
        # check left
        if x > 1 and self.state[x-1,y] == self.opponent:
            for i in range(x-2, -1, -1):
                if self.state[i,y] == self.turn:
                    for j in range(i+1, x):
                        next_state[j,y] = self.turn
                        d+= wmap[j,y]
                    break
                elif self.state[i,y] == 0:
                    break
        # check right
        if x < 6 and self.state[x+1,y] == self.opponent:
            for i in range(x+2, 8):
                if self.state[i,y] == self.turn:
                    for j in range(x+1, i):
                        next_state[j,y] = self.turn
                        d+= wmap[j,y]
                    break
                elif self.state[i,y] == 0:
                    break
        # check up
        if y > 1 and self.state[x,y-1] == self.opponent:
            for i in range(y-2, -1, -1):
                if self.state[x,i] == self.turn:
                    for j in range(i+1, y):
                        next_state[x,j] = self.turn
                        d+= wmap[x,j]
                    break
                elif self.state[x,i] == 0:
                    break
        # check down

        if y < 6 and self.state[x,y+1] == self.opponent:
            for i in range(y+2, 8):
                if self.state[x,i] == self.turn:
                    for j in range(y+1, i):
                        next_state[x,j] = self.turn
                        d+=wmap[x,j]
                    break
                elif self.state[x,i] == 0:
                    break
        # check up left
        if x > 1 and y > 1 and self.state[x-1,y-1] == self.opponent:
            for i in range(2, min(x,y)+1):
                if self.state[x-i,y-i] == self.turn:
                    for j in range(1, i):
                        next_state[x-j,y-j] = self.turn
                        d+=wmap[x-j,y-j]
                    break
                elif self.state[x-i,y-i] == 0:
                    break
        
        # check up right
        if x < 6 and y > 1 and self.state[x+1,y-1] == self.opponent:
            for i in range(2, min(7-x,y)+1):
                if self.state[x+i,y-i] == self.turn:
                    for j in range(1, i):
                        next_state[x+j,y-j] = self.turn
                        d+=wmap[x+j,y-j]
                    break
                elif self.state[x+i,y-i] == 0:
                    break
        
        # check down left
        if x > 1 and y < 6 and self.state[x-1,y+1] == self.opponent:
            for i in range(2, min(x,7-y)+1):
                if self.state[x-i,y+i] == self.turn:
                    for j in range(1, i):
                        next_state[x-j,y+j] = self.turn
                        d+=wmap[x-j,y+j]
                    break
                elif self.state[x-i,y+i] == 0:
                    break
        
        # check down right
        if x < 6 and y < 6 and self.state[x+1,y+1] == self.opponent:
            for i in range(2, min(7-x,7-y)+1):
                if self.state[x+i,y+i] == self.turn:
                    for j in range(1, i):
                        next_state[x+j,y+j] = self.turn
                        d+=wmap[x+j,y+j]
                    break
                elif self.state[x+i,y+i] == 0:
                    break
        
        # add contribution of move to score
        if d > 0: d+=wmap[x,y]
        
        if d > 0 and in_place:
            # update board
            next_state[x,y] = self.turn
            # update turn
            self.turn = - self.turn
            self.opponent = - self.opponent
            self.state = next_state
        
        return d
    
    def is_allowed(self, x:int, y:int):
        return self.eval_move(x,y) > 0
    
    def play(self, x:int, y:int):
        return self.eval_move(x,y, in_place=True)
    
    def get_allowed_moves(self, display=False):
        # return list of allowed moves
        allowed_moves = []
        for x in range(8):
            for y in range(8):
                if self.is_allowed(x,y):
                    allowed_moves.append((x,y))
        
        if display and len(allowed_moves) > 0:
            # display allowed moves
            allowed_moves_board = self.state.copy()
            for move in allowed_moves:
                allowed_moves_board[move] = 0.8
            plt.imshow(allowed_moves_board)
            plt.show()
            print(f"There are {len(allowed_moves)} allowed moves")
        return allowed_moves

    def eval_game(self, _wmap=np.ones((8,8))):
        """Evaluate all possible moves and return the best one."""
        allowed_moves = self.get_allowed_moves()
        if len(allowed_moves) == 0:
            return None
        # evaluate all possible moves
        scores = []
        for move in allowed_moves:
            scores.append(self.eval_move(move[0], move[1], wmap=_wmap))
        # return best move
        return allowed_moves[np.argmax(scores)]
    
    def get_score(self):
        # return score of board
        return np.sum(self.state == -1), np.sum(self.state == 1)
    
    def __repr__(self):
        # return string representation of board
        return str(self.state)
    
    def show(self):
        # show board
        plt.imshow(self.state, cmap="gray")
        plt.show()
    
    def nb_empty_squares(self) -> int:
        """Returns the number of empty squares on the board."""
        return np.sum(self.state == 0)
    


def parse_game_string(game_string):
    moves_list_str = [game_string[i:i+2] for i in range(0, len(game_string), 2)]
    moves_list = []
    for move_str in moves_list_str:
        x = "abcdefgh".find(move_str[0])
        y = int(move_str[1]) -1
        moves_list.append((x,y))
    return moves_list