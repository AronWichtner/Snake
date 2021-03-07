class Snake:
    def __init__(self):
        self.body = [[10, 10], [10, 11], [10, 12]]
        self.move = [0, 0]
        self.moving = False

    def updateSnake(self):
        newBody = self.body[:-1]
        newHead = [self.body[0][0] + self.move[0], self.body[0][1] + self.move[1]]
        newBody.insert(0, newHead)
        self.body = newBody
