from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600 , 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on is True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect the interaction of snake and the food

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.interacted()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.refresh()
        snake.refresh()

    # game be over when snake interacted with its own tail

    for segment in snake.snakes[1:] :
        if snake.head.distance(segment) < 10 :
            scoreboard.refresh()
            snake.refresh()




screen.exitonclick()