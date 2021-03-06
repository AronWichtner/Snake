import random

class Food:
    def __init__(self):
        self.x = self.generateRandomCoorinate()
        self.y = self.generateRandomCoorinate()
        self.position = [self.x, self.y]

    def generateRandomCoorinate(self):
        x = random.randrange(0, 19)
        return x
