from gameboard import Board
from players.base_player import BasePlayer
from players.random_player import RandomPlayer as rdpl
import matplotlib.pyplot as plt

class Game():

    def __init__(
            self, 
            player1:BasePlayer, 
            player2:BasePlayer, 
            board:Board=None):
        
        self.board = Board() if board is None else board
        self.player1 = player1
        self.player2 = player2

        # set player1 as white
        self.player1.color = -1
        # set player2 as black
        self.player2.color = 1

    
    def autoplay(self, display:bool = False, debug:bool = False):
        moves = 0
        positions_history = []
        #check if no moves are left
        while self.board.nb_empty_squares() > 0:
            r = 0
            # player 1's turn
            if self.board.turn == -1:
                r = self.player1.move(self.board, debug)
            # player 2's turn
            else:
                r = self.player2.move(self.board, debug)
            if r > 0 : 
                moves += 1
                if debug: print(f"Move {moves} - empty squares: {self.board.nb_empty_squares()}")
                if display:
                    positions_history.append(self.board.state.copy())
            else:
                break
        
        if display:
            # Add all positions to a single plot for visualization
            _, ax = plt.subplots(int(moves/4) + 1,4, figsize=(20, 300))
            for i in range(moves):
                u, v = int(i/4), i%4
                ax[u, v].imshow(positions_history[i], cmap="gray")
                ax[u, v].set_title(f"Move {i+1}")
            plt.show()
        
        # checks who won
        score1, score2 = self.board.get_score()
        u= -1 if score1>score2 else 1

        if debug: 
            print(f"White score: {score1}")
            print(f"Black score: {score2}")
            print(f"{'White' if u==-1 else 'Black'} wins !")

        return u
            
    
                    
def main():
    # create a game
    game_board = Board()
    game = Game(rdpl(0, game_board), rdpl(0, game_board), game_board)
    # autoplay the game
    game.autoplay(display=True)

if __name__ == "__main__":
    main()
