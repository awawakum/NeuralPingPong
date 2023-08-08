import pygame

from scenes import MainMenu, MultiGame, SoloGame, AutoGame


class Game:

    m_mainMenu = MainMenu.MainMenu()
    m_soloGame = SoloGame.SoloGame()
    m_multiGame = MultiGame.MultiGame()
    m_autoGame = AutoGame.AutoGame()
    m_mode = 0
    m_clock = pygame.time.Clock()

    def __init__(self):
        self.m_running = True
        self.start()

    def start(self):

        while self.m_running:
            print("Loop")
            if self.m_mode == 0:
                self.m_mode = self.m_mainMenu.createField()
            elif self.m_mode == 1:
                self.m_mode = self.m_soloGame.createField()
            elif self.m_mode == 2:
                self.m_mode = self.m_multiGame.createField()
            elif self.m_mode == 3:
                self.m_mode = self.m_autoGame.createField()
            elif self.m_mode == -1:
                self.m_running = False


if __name__ == '__main__':
    game = Game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
