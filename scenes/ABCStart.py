from abc import ABC, abstractmethod
from movable_objects import Player1, Player2, Ball
import pygame


class ABCStart(ABC):

    m_WEIGHT = 1200
    m_HEIGHT = 900
    m_size = (m_WEIGHT, m_HEIGHT)
    m_screen = pygame.display.set_mode(m_size)

    m_left = Player1.Player1(m_screen)
    m_left.set_borders(75, 325)

    m_right = Player2.Player2(m_screen)
    m_right.set_borders(75, 325)
    m_right.m_isAuto = True

    m_ball = Ball.Ball(m_screen)

    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # для звука

        self.m_clock = pygame.time.Clock()

    def clear(self):
        self.m_screen.fill('#ffffff')

    @abstractmethod
    def createField(self):
        pass
