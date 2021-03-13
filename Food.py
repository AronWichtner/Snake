import random
import os
import pygame


class Food:

    def __init__(self):
        self.x = self.generateRandomCoordinate()
        self.y = self.generateRandomCoordinate()
        self.position = [self.x, self.y]
        self.graphics = pygame.image.load(os.path.join('Graphics/apple.png'))

    def generateRandomCoordinate(self):
        x = random.randrange(0, 19)
        return x
