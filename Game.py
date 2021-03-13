from Snake import *
from Food import *
from Poison import *
from Board import *
import pygame, time, sys

pygame.init()

GRASSGREEN = (160, 231, 93)
APPLERED = (199, 0, 57)
SNAKEGREEN = (51, 156, 70)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.poison = Poison()
        self.board = Board()
        self.screen = pygame.display.set_mode((self.board.cell_size * self.board.cell_number,
                                               self.board.cell_size * self.board.cell_number))

    def checkForSamePositions(self):
        food_on_snake = False
        poison_on_snake = False
        poison_on_food = False
        for element in self.snake.body:
            if self.food.position == element:
                food_on_snake = True
                break
            elif self.poison.position == element:
                poison_on_snake = True
                break
            elif self.poison.position == self.food.position:
                poison_on_food = True
                break
            else:
                continue
        return [food_on_snake, poison_on_snake, poison_on_food]

    def drawSnake(self):
        for part in self.snake.body:
            snake_body = pygame.Rect(part[0] * self.board.cell_size,
                                     part[1] * self.board.cell_size,
                                     self.board.cell_size, self.board.cell_size)
            pygame.draw.rect(self.screen, SNAKEGREEN, snake_body)

    def drawFood(self):
        food_rect = pygame.Rect(self.food.position[0] * self.board.cell_size,
                                self.food.position[1] * self.board.cell_size,
                                self.board.cell_size, self.board.cell_size)
        self.screen.blit(self.food.graphics, food_rect)

    def drawPoison(self):
        poison_rect = pygame.Rect(self.poison.position[0] * self.board.cell_size,
                                  self.poison.position[1] * self.board.cell_size,
                                  self.board.cell_size, self.board.cell_size)
        self.screen.blit(self.poison.graphics, poison_rect)

    def drawObjects(self):
        while True:
            positions = self.checkForSamePositions()
            if positions[0]:
                self.food = Food()
                continue
            elif positions[1]:
                self.poison = Poison()
                continue
            elif positions[2]:
                self.poison = Poison()
            else:
                self.drawFood()
                self.drawPoison()
                break
        self.drawSnake()

    def checkForGameOver(self):
        # check if snake ate poison
        if self.checkIfSnakeeatsItslef() or self.movingFromMap():
            return True
        else:
            return False

    def movingFromMap(self):
        if self.snake.body[0][0] < 0 or self.snake.body[0][0] >= 20:
            print("out of map x")
            return True
        elif self.snake.body[0][1] < 0 or self.snake.body[0][1] >= 20:
            print("out of map y")
            return True
        else:
            return False

    def checkIfSnakeeatsItslef(self):
        eatsitself = False
        for element in self.snake.body[1:]:
            if self.snake.body[0] == element:
                print("u ate urself!")
                eatsitself = True
                break
            else:
                continue
        return eatsitself

    def endGame(self):
        self.snake.moving = False
        # print big Game Over sign
        # new game or end (button?)
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def checkForCollision(self):
        if self.snake.body[0] == self.food.position:
            self.growSnake()

    def growSnake(self):
        self.food = Food()
        newSnakePart = [self.snake.body[-1][0], self.snake.body[-1][1] + 1]
        self.snake.body.append(newSnakePart)
