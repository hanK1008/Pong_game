from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

# Creating screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating Paddle
user1_paddle = Paddle(350, 0)
user2_paddle = Paddle(-350, 0)

# Creating Ball
ball = Ball()


# Listening to input
screen.listen()
screen.onkeypress(user1_paddle.move_up, "Up")
screen.onkeypress(user1_paddle.move_down, "Down")
screen.onkeypress(user2_paddle.move_up, "w")
screen.onkeypress(user2_paddle.move_down, "s")

game_on = True

while game_on:
    sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 290:
        ball.right(90)
    elif ball.ycor() <= -290:
        ball.left(90)


screen.exitonclick()


