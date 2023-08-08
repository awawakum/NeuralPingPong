from .ABCStart import ABCStart, pygame


class MainMenu(ABCStart):

    def __init__(self):
        super().__init__()

        self.m_soloGamePosRect = [self.m_WEIGHT/4, self.m_HEIGHT * 2 / 16,
                                  self.m_WEIGHT * 2 / 4, self.m_HEIGHT * 2 / 16]
        self.m_soloGamePosText = [self.m_soloGamePosRect[0] + self.m_soloGamePosRect[0] / 4,
                                  self.m_soloGamePosRect[1] + self.m_soloGamePosRect[1] / 4]

        self.m_multiGamePosRect = [self.m_WEIGHT / 4, self.m_HEIGHT * 6 / 16,
                                   self.m_WEIGHT * 2 / 4, self.m_HEIGHT * 2 / 16]
        self.m_multiGamePosText = [self.m_multiGamePosRect[0] + self.m_multiGamePosRect[0] / 4,
                                   self.m_multiGamePosRect[1] + self.m_multiGamePosRect[1] / 12]

        self.m_autoGamePosRect = [self.m_WEIGHT / 4, self.m_HEIGHT * 10 / 16,
                                  self.m_WEIGHT * 2 / 4, self.m_HEIGHT * 2 / 16]
        self.m_autoGamePosText = [self.m_autoGamePosRect[0] + self.m_autoGamePosRect[0] / 4,
                                  self.m_autoGamePosRect[1] + self.m_autoGamePosRect[1] / 20]

    # Отрисовка главного меню
    def paintMenu(self):

        self.m_screen.fill('#ffffff')

        pygame.draw.rect(self.m_screen,
                         color=(1, 1, 1),
                         rect=self.m_soloGamePosRect)

        font = pygame.font.SysFont('consolas', 55)
        text = font.render('Одиночная игра', True,
                          (255, 255, 255))
        self.m_screen.blit(text, self.m_soloGamePosText)

        pygame.draw.rect(self.m_screen,
                         color=(1, 1, 1),
                         rect=self.m_multiGamePosRect)

        text = font.render('Совместная игра', True,
                           (255, 255, 255))
        self.m_screen.blit(text, self.m_multiGamePosText)

        pygame.draw.rect(self.m_screen,
                         color=(1, 1, 1),
                         rect=self.m_autoGamePosRect)

        text = font.render('Бот против бота', True,
                           (255, 255, 255))
        self.m_screen.blit(text, self.m_autoGamePosText)

    def createField(self):

        self.m_running = True

        pygame.display.set_caption("mainMenu")

        self.paintMenu()

        while self.m_running:
            # Держим цикл на правильной скорости
            self.m_clock.tick(30)
            # после отрисовки всего, переворачиваем экран
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.m_soloGamePosRect[0] < event.pos[0] < self.m_soloGamePosRect[0] + self.m_soloGamePosRect[2]:
                            if self.m_soloGamePosRect[1] < event.pos[1] < self.m_soloGamePosRect[1] + self.m_soloGamePosRect[3]:
                                self.m_running = False
                                return 1
                        if self.m_multiGamePosRect[0] < event.pos[0] < self.m_multiGamePosRect[0] + self.m_multiGamePosRect[2]:
                            if self.m_multiGamePosRect[1] < event.pos[1] < self.m_multiGamePosRect[1] + self.m_multiGamePosRect[3]:
                                self.m_running = False
                                return 2
                        if self.m_autoGamePosRect[0] < event.pos[0] < self.m_autoGamePosRect[0] + self.m_autoGamePosRect[2]:
                            if self.m_autoGamePosRect[1] < event.pos[1] < self.m_autoGamePosRect[1] + self.m_autoGamePosRect[3]:
                                self.m_running = False
                                return 3
                if event.type == pygame.QUIT:
                    self.m_running = False
                    return -1
