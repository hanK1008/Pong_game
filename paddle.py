from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position, y_position)
        self.speed("fastest")
        self.starting_x_position = x_position
        self.starting_y_position = y_position

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def paddle_reset(self):
        self.goto(self.starting_x_position, self.starting_y_position)


