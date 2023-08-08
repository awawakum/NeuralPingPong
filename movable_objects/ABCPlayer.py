from .MovableObject import ABCMovableObject
from abc import abstractmethod
import pygame


class ABCPlayer(ABCMovableObject):

    m__topBorderRect = (50, 50, 500, 25)
    m_botBorderRect = (50, 325, 500, 25)

    m_rectPos = [0, 0, 0, 0]
    m_color = (0, 0, 0)
    m_borders = [0, 0]

    m_record = 0

    m_isAuto = True

    def up(self):
        if self.m_rectPos[1] > self.m_borders[0]:
            self.m_rectPos[1] -= 25

    def down(self):
        if self.m_rectPos[1] + self.m_rectPos[3] < self.m_borders[1]:
            self.m_rectPos[1] += 25

    def set_borders(self, y_top, y_bot):
        self.m_borders = [y_top, y_bot]

    def record_up(self):
        self.m_record += 1

    @abstractmethod
    def update(self):
        pass