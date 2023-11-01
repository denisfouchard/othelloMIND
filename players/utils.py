import numpy as np
from gameboard import Board

def build_wmap() -> np.ndarray:
    wmap = np.ones((8, 8))

    # Add weights to the four edges
    wmap[0, :] += 1
    wmap[7, :] += 1
    wmap[:, 0] += 1
    wmap[:, 7] += 1

    # Add weights to the four corners
    wmap[0, 0] += 3
    wmap[0, 7] += 3
    wmap[7, 0] += 3
    wmap[7, 7] += 3

    return wmap

def minmax_heuristic(board:Board, color:int) -> int:
    """Heuristic for minmax algorithm"""
    return np.sum(board.state == color) - np.sum(board.state == -color)