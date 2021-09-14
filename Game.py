from Consts import *

class Snake:

    def __init__(self, x, y, *, bodyLen=GROWING_SPEED, body=[]) -> None:
        self.head = [x, y]
        self.bodyLen = bodyLen 
        self.body = body

    @property
    def x(self):
        return self.head[0]
    @x.setter
    def x(self, value):
        assert isinstance(value, int), "x has to be of type int, " + str(type(value).__name__) + " detected."
        self.head[0] = value
    @property
    def y(self):
        return self.head[1]
    @y.setter
    def y(self, value):
        self.head[1] = value

class Game:

    def __init__(self) -> None:
        self.board = [[0 for i in range(COLS)] for j in range(ROWS)]
        self.snake        

if __name__ == '__main__':
    snake = Snake(3,5)
    print(snake.head)
    snake.x = 1.2
    snake.y = 8
    print(snake.head)