from .ABCPlayer import ABCPlayer, pygame
from .Brain import Brain


class Player2(ABCPlayer):

    m_brain = Brain.Brain()

    def __init__(self, screen):
        self.m_rectPos = [525, 150, 25, 50]
        self.m_screen = screen

    def update(self):
        pygame.draw.rect(self.m_screen, rect=self.m_rectPos, color=self.m_color)
