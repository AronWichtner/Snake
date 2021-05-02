from Snake import *
from Food import *
from Poison import *
from Board import *
from Score import *
import pygame
import time
import sys

pygame.init()

#colours
GRASSGREEN = (160, 231, 93)
APPLERED = (199, 0, 57)
SNAKEGREEN = (51, 156, 70)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.poison = Poison()
        self.board = Board()
        self.score = Score()
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

    def drawScore(self):
        scorefont = pygame.font.Font(None, 100)
        scoreimg = scorefont.render(str(self.score.score), True, (79, 21, 21))
        score_rect = pygame.Rect(18 * self.board.cell_size, 18 * self.board.cell_size,
                                 self.board.cell_size, self.board.cell_size)
        self.screen.blit(scoreimg, score_rect)

    def drawObjects(self):
        while True:
            positions = self.checkForSamePositions()
            if positions[0]:  # food on snake
                self.food = Food()
                continue
            elif positions[1]:  # poison in snake
                self.poison = Poison()
                continue
            elif positions[2]:  # poison in food
                self.poison = Poison()
                continue
            else:
                self.drawFood()
                self.drawPoison()
                break
        self.drawScore()
        self.drawSnake()

    def checkForGameOver(self):
        if self.checkIfSnakeeatsItslef() or self.movingFromMap() or self.checkIfeatPoison():
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

    def checkIfeatPoison(self):
        if self.poison.position == self.snake.body[0]:
            return True

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

    def checkAndHandleCollision(self):
        if self.snake.body[0] == self.food.position:
            self.growSnake()
            self.score.update_score()

    def growSnake(self):
        self.food = Food()
        newSnakePart = [self.snake.body[-1][0], self.snake.body[-1][1] + 1]
        self.snake.body.append(newSnakePart)

    def endGame(self):
        self.snake.moving = False
        print(self.score.score)
        self.draw_game_over()
        pygame.display.update()
        # new game or end (button?)
        time.sleep(3)
        pygame.quit()
        sys.exit()

    def draw_game_over(self):
        game_over_font = pygame.font.Font(None, 100)
        game_over_img = game_over_font.render("Game Over!", True, (0, 0, 0))
        self.screen.blit(game_over_img, (5 * self.board.cell_size, 9 * self.board.cell_size))

        final_score_font = pygame.font.Font(None, 50)
        final_score_img = final_score_font.render("Final Score: {}".format(str(self.score.score)), True, (79, 21, 21))
        self.screen.blit(final_score_img, (7 * self.board.cell_size, 11 * self.board.cell_size))




