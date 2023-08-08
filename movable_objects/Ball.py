from .ABCPlayer import ABCPlayer, pygame
import random
from .MovableObject import ABCMovableObject


class Ball(ABCMovableObject):

    m_direction = [0, 0]
    m_speed = 0
    m_rectPlayer1 = [0, 0, 0, 0]
    m_rectPlayer2 = [0, 0, 0, 0]
    m_inArea = True

    def __init__(self, screen):
        self.m_color = [0, 0, 0]
        self.m_rectPos = [286, 185, 25, 25]
        self.m_screen = screen
        self.set_mode()

    def set_players_position_rects(self, rectPlayer1, rectPlayer2):
        self.m_rectPlayer1 = rectPlayer1
        self.m_rectPlayer2 = rectPlayer2

    def set_mode(self, speed=5):
        self.m_speed = speed
        while self.m_direction[0] == 0 or self.m_direction[1] == 0:
            self.m_direction = [random.randint(-1, 1) * self.m_speed, random.randint(-1, 1) * self.m_speed]

    def update(self):

        if self.m__topBorderRect[1]+self.m__topBorderRect[3] >= self.m_rectPos[1]:
            self.top_rebound()
        if self.m_botBorderRect[1] <= self.m_rectPos[1]+self.m_rectPos[3]:
            self.bot_rebound()

        if self.m_rectPlayer1[0]+self.m_rectPlayer1[2] >= self.m_rectPos[0]:
            if self.m_rectPlayer1[1] - self.m_rectPos[3] <= self.m_rectPos[1] <= self.m_rectPlayer1[1] + self.m_rectPlayer1[3]:
                self.left_rebound()

        if self.m_rectPlayer2[0] <= self.m_rectPos[0] + self.m_rectPos[2]:
            if self.m_rectPlayer2[1] - self.m_rectPos[3] <= self.m_rectPos[1] <= self.m_rectPlayer2[1] + self.m_rectPlayer2[3]:
                self.right_rebound()

        if self.m_rectPlayer1[0] + self.m_rectPlayer1[2] > self.m_rectPos[0] + 5:
            self.m_inArea = False
            self.m_rectPos = [286, self.m_rectPos[1], 25, 25]
            self.right_rebound()
            return -1

        if self.m_rectPlayer2[0] + 1 < self.m_rectPos[0]+self.m_rectPos[2]:
            self.m_inArea = False
            self.m_rectPos = [286, self.m_rectPos[1], 25, 25]
            self.right_rebound()
            return 1

        self.m_rectPos[0] += self.m_direction[0]
        self.m_rectPos[1] += self.m_direction[1]

        pygame.draw.rect(self.m_screen, rect=self.m_rectPos, color=self.m_color)
        self.m_inArea = True
        return 0

    def top_rebound(self):
        self.m_direction = [self.m_direction[0], -self.m_direction[1]]

    def bot_rebound(self):
        self.m_direction = [self.m_direction[0], -self.m_direction[1]]

    def left_rebound(self):
        self.m_direction = [-self.m_direction[0], self.m_direction[1]]

    def right_rebound(self):
        self.m_direction = [-self.m_direction[0], self.m_direction[1]]

    def createField(self):
        pass