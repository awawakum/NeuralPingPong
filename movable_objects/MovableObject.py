from abc import ABC, abstractmethod
import pygame


class ABCMovableObject(ABC):

    m__topBorderRect = (50, 50, 500, 25)
    m_botBorderRect = (50, 325, 500, 25)

    @abstractmethod
    def update(self):
        pass