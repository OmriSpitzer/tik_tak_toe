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


class TicTacTowBuilder(Builder):
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

    def check_win(self):
        import color as cl
        win_positions = self.check_win_by_mat()

        if win_positions:
            cell_size = self._board_width // 3  # Convert matrix indices to pixel positions

            # Convert board indices (row, col) to pixel positions
            start_x = win_positions[0][1] * cell_size + cell_size // 2
            start_y = win_positions[0][0] * cell_size + cell_size // 2
            end_x = win_positions[1][1] * cell_size + cell_size // 2
            end_y = win_positions[1][0] * cell_size + cell_size // 2

            pygame.draw.line(self._surface, cl.Color.BLACK.value, (start_x, start_y), (end_x, end_y), 5)
            return True  # A win has been detected

        return False  # No win detected

    def check_win_by_mat(self):
        check_arr = self._result.get_matrix()

        # Check rows
        for i in range(3):
            if check_arr[i][0] is not None and check_arr[i][0] == check_arr[i][1] == check_arr[i][2]:
                return [(i, 0), (i, 2)]  # Row win

        # Check columns
        for i in range(3):
            if check_arr[0][i] is not None and check_arr[0][i] == check_arr[1][i] == check_arr[2][i]:
                return [(0, i), (2, i)]  # Column win

        # Check main diagonal
        if check_arr[0][0] is not None and check_arr[0][0] == check_arr[1][1] == check_arr[2][2]:
            return [(0, 0), (2, 2)]  # Main diagonal win

        # Check anti-diagonal
        if check_arr[0][2] is not None and check_arr[0][2] == check_arr[1][1] == check_arr[2][0]:
            return [(0, 2), (2, 0)]  # Anti-diagonal win

        return None  # No win found

