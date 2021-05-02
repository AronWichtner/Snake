from Game import *

game = Game()

clock = pygame.time.Clock()  # for FPS
SNAKE_UPDATE = pygame.USEREVENT  # creating a user-event
pygame.time.set_timer(SNAKE_UPDATE, 100)  # game speed
snakeStartedMove = False  # no updateSnake() before snake moved


def handleKeyPress():
    if event.key == pygame.K_UP:
        if game.snake.move[1] == 1:
            pass
        else:
            game.snake.move[0] = 0
            game.snake.move[1] = -1
    elif event.key == pygame.K_DOWN:
        if game.snake.move[1] == -1:
            pass
        else:
            game.snake.move[0] = 0
            game.snake.move[1] = 1
    elif event.key == pygame.K_RIGHT:
        if game.snake.move[0] == -1:
            pass
        else:
            game.snake.move[1] = 0
            game.snake.move[0] = 1
    elif event.key == pygame.K_LEFT:
        if game.snake.move[0] == 1:
            pass
        else:
            game.snake.move[1] = 0
            game.snake.move[0] = -1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game.snake.moving:
            if event.type == SNAKE_UPDATE:
                game.snake.updateSnake()
                gameOver = game.checkForGameOver()
                if gameOver:
                    game.endGame()
                    pygame.display.update()
                game.checkAndHandleCollision()
        if event.type == pygame.KEYDOWN:
            if not game.snake.moving:
                if event.key == pygame.K_DOWN:
                    pass
                else:
                    game.snake.moving = True
                    handleKeyPress()
            else:
                game.snake.moving = True
                handleKeyPress()
    game.screen.fill(GRASSGREEN)
    game.drawObjects()
    pygame.display.update()
    clock.tick(60)

