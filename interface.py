import pygame
import sys
import time
import random
import numpy as np
import board
import players.player as player
from players.greedy_player import GreedyPlayer
from players.random_player import RandomPlayer
from players.montecarlo_player import MonteCarloPlayer
from players.default_player import DefaultPlayer
from game import Game


# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

# Set the width and height of the screen [width, height]
size = (600, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Othello")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# create a game
game_board = board.Board()

# create players
computer_player = GreedyPlayer(1, game_board)
human_player = DefaultPlayer(-1, game_board)

# create a game
game = Game(computer_player, human_player, game_board)

# Function to draw the current board
def draw_board(game_board):
    # Draw the grid
    for row in range(8):
        for column in range(8):
            color = BLACK
            if game_board.state[row, column] == -1:
                color = WHITE
            elif game_board.state[row, column] == 1:
                color = BLACK
            elif game_board.state[row, column] == 0:
                color = GREY
            pygame.draw.rect(screen,
                             color,
                             [(size[0] // 8) * column,
                              (size[1] // 8) * row,
                              size[0] // 8,
                              size[1] // 8])
    # Draw the grid lines
    for row in range(9):
        pygame.draw.line(screen,
                         BLACK,
                         (0, (size[1] // 8) * row),
                         (size[0], (size[1] // 8) * row),
                         1)
    for col in range(9):
        pygame.draw.line(screen,
                         BLACK,
                         ((size[0] // 8) * col, 0),
                         ((size[0] // 8) * col, size[1]),
                         1)
    pygame.display.flip()


# -------- Main Program Loop -----------
while not done:
    draw_board(game_board)

    # --- Main event loop --- 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (size[0] // 8)
            row = pos[1] // (size[1] // 8)
            # print("Click ", pos, "Grid coordinates: ", row, column)
            d = game_board.play(row, column)
            if d == -1:
                continue
            
            # Freeze the board for 1 second in order to see the move
            
            # Compute the computer's move
            x = computer_player.move(game_board)
            if x == -1:
                print("No valid move for the computer")
            elif x == -2:
                print("It is not the computer's turn")

            # Switch the turn to the computer player's color

            # Check if the game is over
            if game_board.nb_empty_squares() == 0:
                print("Game over")

            
            # Check if the game is over
            if game_board.nb_empty_squares() == 0:
                score1, score2 = game_board.get_score()
                if score1 > score2:
                    print("White wins!")
                elif score2 > score1:
                    print("Black wins!")
                else:
                    print("Draw!")
                done = True


            






