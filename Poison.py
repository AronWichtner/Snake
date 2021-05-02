import random
import pygame
import os

class Poison:

    def __init__(self):
        self.x = self.gernerateRandomCoordinate()
        self.y = self.gernerateRandomCoordinate()
        self.position = [self.x, self.y]
        self.graphics = pygame.image.load(os.path.join('Graphics/poison.png'))

    def gernerateRandomCoordinate(self):
        x = random.randrange(0, 19)
        return x
