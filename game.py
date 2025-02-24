import pygame
import gameBuilder
import gameDirector as direc


class Game:
    def __init__(self):
        pygame.init()
        self._game_builder = gameBuilder.TikTakToeBuilder(400, 400, 400)
        self._director = direc.GameDirector(self._game_builder)

        self._running = True

        pygame.display.set_caption("Tik-Tak-Toe")

    def run(self):
        self._director.make_game()

        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    cell_size = self._game_builder.getResult().get_board_width() // 3
                    row, col = y // cell_size, x // cell_size

                    play = self._director.handle_player_click(row, col)

                    if play and not self._director.check_full():
                        self._director.handle_computer_click()

            pygame.display.flip()

        pygame.quit()
