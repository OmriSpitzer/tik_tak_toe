from abc import ABC, abstractmethod
import pygame
import shapes as sh


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_shape(self, x_index, y_index, shape: sh.Shape):
        pass

    @abstractmethod
    def build_player(self, name):
        pass

    @abstractmethod
    def build_board(self):
        pass

    @abstractmethod
    def show_board(self):
        pass


class Player:
    def __init__(self, name="Jon Doe", shape=None):
        self._name = name
        self._shape = shape

    def get_shape(self):
        return self._shape

    def get_name(self):
        return self._name


class Board:
    def __init__(self, board_width=300):
        self._mat = [[None for _ in range(3)] for _ in range(3)]
        self._board_width = board_width

    def get_board_width(self):
        return self._board_width

    def change_cell(self, row, col, shape):
        if self._mat[row][col] is None:  # Only allow moves in empty spaces
            self._mat[row][col] = shape

    def get_matrix(self):
        return self._mat


class TikTakToeBuilder(Builder):
    def __init__(self, width, height, board_width):
        self._result = None
        self._board_width = board_width
        self._surface = pygame.display.set_mode((width, height))
        self.reset()

    def getResult(self):
        return self._result

    def reset(self):
        self._result = Board(self._board_width)

    def build_shape(self, x_index, y_index, shape: sh.Shape):
        shape.draw(self._surface, x_index, y_index)

    def build_player(self, name, cl=None):
        import color as cl

        if name == "Computer":
            return Player(name, sh.Circle(self._board_width // 9, cl.Color.RED))
        return Player(name, sh.Cross(self._board_width // 4.5, cl.Color.BLUE))

    def build_board(self):
        self.reset()

    def show_board(self):
        for i in range(3):
            for j in range(3):
                square_length = self._board_width // 3
                x_axis = square_length * j
                y_axis = square_length * i

                self.build_shape(x_axis, y_axis, sh.Square(square_length))

                if self.getResult().get_matrix()[i][j]:
                    shape_x_axis = x_axis + square_length // 6
                    shape_y_axis = y_axis + square_length // 6
                    self.build_shape(shape_x_axis, shape_y_axis, self.getResult().get_matrix()[i][j])
