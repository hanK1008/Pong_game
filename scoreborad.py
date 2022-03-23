from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("courier", 60, "normal"))
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("courier", 60, "normal"))

    def score_goes_to_left(self):
        self.l_score += 1
        self.update_score()

    def score_goes_to_right(self):
        self.r_score += 1
        self.update_score()
