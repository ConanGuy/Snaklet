from Consts import *
from math import ceil
from locate import locate
from random import choice
import keyboard
from time import sleep

class Snake:

    def __init__(self, x, y, *, bodyLen=GROWING_SPEED, body=[]) -> None:
        self.head = [x, y]
        self.bodyLen = bodyLen 
        self.body = body
        self.direction = None

    @property
    def x(self) -> int:
        return self.head[0]
    @x.setter
    def x(self, value) -> None:
        assert isinstance(value, int), "x has to be of type int, " + str(type(value).__name__) + " detected."
        self.head[0] = value
    @property
    def y(self) -> int:
        return self.head[1]
    @y.setter
    def y(self, value) -> None:
        assert isinstance(value, int), "y has to be of type int, " + str(type(value).__name__) + " detected."
        self.head[1] = value

    def move(self) -> None:
        if not self.direction:
            return

        if not self.bodyLen > len(self.body):
            self.body.pop(0)
        self.body.append(tuple(self.head))
        

        directionArray = DIRECTION_ARRAYS[DIRECTION_INDEXES[self.direction]]
        self.head[directionArray[0]] += directionArray[1]

class Game:

    def __init__(self) -> None:
        self.board = [[0 for i in range(COLS)] for j in range(ROWS)]
        self.snake = Snake(ceil(COLS/2), ceil(ROWS/2))        
        self.apple = self.new_apple()

    def new_apple(self) -> tuple:
        xArray = [i for i in range(1,COLS+1) if i not in [j[0] for j in self.snake.body]+[self.snake.x]]
        yArray = [i for i in range(1,ROWS+1) if i not in [j[1] for j in self.snake.body]+[self.snake.y]]

        x = choice(xArray)
        y = choice(yArray)

        return (x, y)

    def snake_is_alive(self) -> bool:
        return 1 <= self.snake.x <= COLS and 1 <= self.snake.y <= ROWS and tuple(self.snake.head) not in self.snake.body

    def snake_is_eating(self) -> bool:
        return tuple(self.snake.head) == self.apple 

    def run(self) -> None:
        running = True
        while running:
            sleep(1)

            if keyboard.is_pressed("z"):
                self.snake.direction  = "up"
            if keyboard.is_pressed("q"):
                self.snake.direction  = "left"
            if keyboard.is_pressed("s"):
                self.snake.direction  = "down"
            if keyboard.is_pressed("d"):
                self.snake.direction  = "right"
    
            self.snake.move()
            if self.snake_is_eating():
                self.apple = self.new_apple()
                self.snake.bodyLen += GROWING_SPEED

            running = self.snake_is_alive()

            print(self)
        print("LOSER")

    def __str__(self) -> str:
        s = ""

        s = locate(s, "+"+COLS*'-'+"+", 0, 0)
        for i in range(ROWS):
            s = locate(s, "|"+COLS*' '+"|", 0, i+1, ignore=[' '])
        s = locate(s, "+"+COLS*'-'+"+", 0, ROWS+1)

        for b in self.snake.body:
            s = locate(s, "B", b[0], b[1])
        s = locate(s, "T", self.snake.x, self.snake.y)
        s = locate(s, "A", self.apple[0], self.apple[1])

        return s

if __name__ == '__main__':
    game = Game()
    game.run()