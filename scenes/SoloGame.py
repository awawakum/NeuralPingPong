from .ABCStart import ABCStart, pygame
###
import numpy as np
from matplotlib import pyplot as plt


class SoloGame(ABCStart):

    def __init__(self):
        super().__init__()

    def createField(self):

        self.clear()

        self.m_running = True
        pygame.display.set_caption("SoloGame")

        bounces = 0

        while self.m_running:
            # Держим цикл на правильной скорости
            self.m_clock.tick(120)

            self.clear()

            pygame.draw.rect(self.m_screen, rect=(50, 50, 500, 25), color=(0, 0, 0))

            font = pygame.font.SysFont('consolas', 38)

            text = font.render(str(self.m_left.m_record), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (50, 10, 20, 20))

            text = font.render(str(bounces), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (530, 10, 20, 20))

            pygame.draw.rect(self.m_screen, rect=(50, 325, 500, 25), color=(0, 0, 0))



            self.m_left.update()
            self.m_right.update()
            self.m_ball.set_players_position_rects(self.m_left.m_rectPos, self.m_right.m_rectPos)

            bounce_cords = [(self.m_ball.m_rectPos[0]) / 400,
                            (self.m_ball.m_rectPos[1]) / 400,
                            (self.m_ball.m_direction[0]) / 10,
                            self.m_right.m_rectPos[1] / 400]

            z = self.m_right.m_brain.predict(np.array(bounce_cords))
            y_pred = np.argmax(z)

            if y_pred == 0:
                self.m_right.up()
            if y_pred == 1:
                pass
                #print("STAY")
            if y_pred == 2:
                self.m_right.down()

            ret = self.m_ball.update()

            if self.m_ball.m_rectPlayer2[0] <= self.m_ball.m_rectPos[0] + self.m_ball.m_rectPos[2]:
                if self.m_ball.m_rectPlayer2[1] - self.m_ball.m_rectPos[3] <= self.m_ball.m_rectPos[1] <= self.m_ball.m_rectPlayer2[1] + \
                        self.m_ball.m_rectPlayer2[3]:
                    bounce_cords = [(self.m_ball.m_rectPos[0] - self.m_ball.m_direction[0]) / 400,
                                    (self.m_ball.m_rectPos[1]) / 400,
                                    (self.m_ball.m_direction[0]) / 10,
                                    self.m_right.m_rectPos[1] / 400]
                    x = np.array([bounce_cords])
                    print("->>>BOUNCE")
                    bounces += 1
                    y = np.array([0, 1, 0])
                    self.m_right.m_brain.train(x, y)

            if ret == 1:
                bounce_cords = [(self.m_ball.m_rectPos[0] - self.m_ball.m_direction[0]) / 400,
                                (self.m_ball.m_rectPos[1]) / 400,
                                (self.m_ball.m_direction[0]) / 10,
                                self.m_right.m_rectPos[1] / 400]
                x = np.array([bounce_cords])
                if self.m_ball.m_rectPos[1] <= self.m_right.m_rectPos[1]:
                    print("->>>UPPER")
                    y = np.array([1, 0, 0])
                    self.m_right.m_brain.train(x, y)
                if self.m_ball.m_rectPos[1] >= self.m_right.m_rectPos[1]:
                    print("->>>UNDER")
                    y = np.array([0, 0, 1])
                    self.m_right.m_brain.train(x, y)
                self.m_left.record_up()

            if ret == -1:
                self.m_right.record_up()

            font = pygame.font.SysFont('consolas', 13)
            text = font.render('W1[0] : ' + str(self.m_left.m_brain.W1[0]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (25, 500, 100, 100))

            text = font.render('W1[1] : ' + str(self.m_left.m_brain.W1[1]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (25, 600, 100, 100))

            text = font.render('W1[2] : ' + str(self.m_left.m_brain.W1[2]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (25, 700, 100, 100))

            text = font.render('W1[3] : ' + str(self.m_left.m_brain.W1[3]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (25, 800, 100, 100))

            font = pygame.font.SysFont('consolas', 13)

            text = font.render('W2[0] : ' + str(self.m_right.m_brain.W2[0]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (625, 500, 100, 100))

            text = font.render('W2[1] : ' + str(self.m_right.m_brain.W2[2]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (625, 600, 100, 100))

            text = font.render('W2[2] : ' + str(self.m_right.m_brain.W2[3]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (625, 700, 100, 100))

            text = font.render('W2[3] : ' + str(self.m_right.m_brain.W2[4]), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (625, 800, 100, 100))

            font = pygame.font.SysFont('consolas', 10)

            text = font.render('RIGHT Z : ' + str(z), True,
                               (0, 0, 0))
            self.m_screen.blit(text, (800, 200, 100, 100))

            font = pygame.font.SysFont('consolas', 13)

            # после отрисовки всего, переворачиваем экран
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.m_left.up()
                    if event.key == pygame.K_s:
                        self.m_left.down()

                if event.type == pygame.QUIT:
                    plt.plot(self.m_right.m_brain.get_lossArr())
                    plt.show()
                    self.m_running = False
        return 0