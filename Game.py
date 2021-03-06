from Snake import *
from Food import *
from Board import *
import pygame

pygame.init()

GRASSGREEN = (160, 231, 93)
APPLERED = (199, 0, 57)
SNAKEGREEN = (51, 156, 70)


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.board = Board()
        self.screen = pygame.display.set_mode((self.board.cell_size * self.board.cell_number,
                                               self.board.cell_size * self.board.cell_number))

    def drawObjects(self):
        fruit_rect = pygame.Rect(self.food.position[0] * self.board.cell_size,
                                 self.food.position[1] * self.board.cell_size,
                                 self.board.cell_size, self.board.cell_size)
        pygame.draw.rect(self.screen, APPLERED, fruit_rect)

        for part in self.snake.body:
            snake_body = pygame.Rect(part[0] * self.board.cell_size,
                                     part[1] * self.board.cell_size,
                                     self.board.cell_size, self.board.cell_size)
            pygame.draw.rect(self.screen, SNAKEGREEN, snake_body)

    def checkForCollision(self):
        if self.snake.body[0] == self.food.position:
            self.handleCollision()

    def handleCollision(self):
        self.food = Food()
        newSnakePart = [self.snake.body[-1][0], self.snake.body[-1][1] + 1]
        self.snake.body.append(newSnakePart)
