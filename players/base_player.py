from gameboard import Board
from abc import ABC, abstractmethod

class BasePlayer(ABC):
    """Abstract class for a player"""
    def __init__(self, color:int, board:Board):
        self.color = color

    @abstractmethod
    def move(self, board:Board, debug:bool = False):
        pass
