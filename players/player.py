import board
import numpy as np
import abc

class Player(abc.ABC):
    """Abstract class for a player"""
    def __init__(self, color:int, board:board.Board):
        self.color = color

    @abc.abstractmethod
    def move(self, board:board.Board, debug:bool = False):
        pass
