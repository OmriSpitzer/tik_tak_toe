from gameBuilder import Builder, TicTacTowBuilder
import random


class GameDirector:
    def __init__(self, builder: Builder):
        self._board = None
        self._builder = builder
        self._computer = None
        self._player = None

    def change_builder(self, new_builder: Builder):
        self._builder = new_builder

    def make_game(self):
        if isinstance(self._builder, TicTacTowBuilder):
            self._builder.build_board()
            self._computer = self._builder.build_player("Computer")
            self._player = self._builder.build_player("Omri Spitzer")
            self._builder.show_board()
            self._board = self._builder.getResult()

    def get_builder(self):
        return self._builder

    def handle_player_click(self, row, col):
        if self._board.get_matrix()[row][col] is None:
            self._board.change_cell(row, col, self._player.get_shape())
            self._builder.show_board()
            return True
        else:
            return False

    def handle_computer_click(self):
        empty_places = self.generate_empty_places_array()

        rand_number = random.randint(0, len(empty_places) - 1)
        row, col = empty_places[rand_number]

        self._board.change_cell(row, col, self._computer.get_shape())
        self._builder.show_board()

    def generate_empty_places_array(self):
        empty_places = []
        for i in range(3):
            for j in range(3):
                if not self._board.get_matrix()[i][j]:
                    empty_places.append((i, j))
        return empty_places

    def check_full(self):
        empty_places = self.generate_empty_places_array()
        return len(empty_places) == 0


