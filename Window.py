import pyglet
from Game import Game, Snake
from Consts import *
from time import sleep 

class GameWindow(pyglet.window.Window):

    def __init__(self, width, height, game=Game()) -> None:
        super().__init__(width, height)
        self.game = game

    @property
    def snake(self) -> Snake:
        return self.game.snake
    @property
    def apple(self) -> tuple:
        return self.game.apple

    def on_draw(self):
        self.clear()
        for i in range(ROWS):
            for j in range(COLS):
                x, y = j*CASE_SIZE, i*CASE_SIZE
                pyglet.shapes.Rectangle(x, y, CASE_SIZE, CASE_SIZE, color=(0,0,0)).draw()
        
        x, y = self.snake.x*CASE_SIZE, self.snake.y*CASE_SIZE
        pyglet.shapes.Rectangle(x, y, CASE_SIZE, CASE_SIZE, color=(0,255,0)).draw()
        
        x, y = self.apple[0]*CASE_SIZE, self.apple[1]*CASE_SIZE
        pyglet.shapes.Rectangle(x, y, CASE_SIZE, CASE_SIZE, color=(255,0,0)).draw()

if __name__ == "__main__":
    window = GameWindow(COLS*CASE_SIZE, ROWS*CASE_SIZE)
    pyglet.app.run()