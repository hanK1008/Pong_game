from turtle import Turtle
from time import sleep


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def right_user_lose(self):
        self.goto(0, 0)
        # sleep(1)

    def left_user_loose(self):
        self.goto(0, 0)
        # sleep(1)

    def reverse_move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move

        self.goto(new_x, new_y)
