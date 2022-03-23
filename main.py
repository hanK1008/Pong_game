from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreborad import ScoreBoard

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
# Creating scoreboard
scoreboard = ScoreBoard()

# Creating middle Line
y_axis = -450
for l in range(10):
    l = Turtle()
    l.shape("square")
    l.color("white")
    l.shapesize(stretch_wid=2.5, stretch_len=0.25)
    l.penup()
    y_axis += 100
    l.goto(0, y_axis)
# Middle Line complete


# Listening to input
screen.listen()
screen.onkeypress(user1_paddle.move_up, "Up")
screen.onkeypress(user1_paddle.move_down, "Down")
screen.onkeypress(user2_paddle.move_up, "w")
screen.onkeypress(user2_paddle.move_down, "s")

game_on = True
time_fast = 0.1
while game_on:

    sleep(time_fast)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.distance(user1_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
        time_fast -= 0.01
    if ball.distance(user2_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # Detecting ball missing the paddle
    if ball.xcor() > 380:
        sleep(1)
        ball.reset_position()
        user1_paddle.paddle_reset()
        user2_paddle.paddle_reset()
        scoreboard.score_goes_to_left()
        screen.update()
        time_fast = 0.1
        sleep(1)

    if ball.xcor() < -380:
        sleep(1)
        ball.reset_position()
        user1_paddle.paddle_reset()
        user2_paddle.paddle_reset()
        scoreboard.score_goes_to_right()
        screen.update()
        time_fast = 0.1
        sleep(1)

screen.exitonclick()


