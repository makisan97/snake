from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('#8090ad')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.snake_parts[0].distance(food) < 20:
        food.refesh()
        snake.extend()
        scoreboard.score_increase()
        
    # Detect collision with wall
    if snake.snake_parts[0].xcor() > 395 or snake.snake_parts[0].xcor() < -395 or snake.snake_parts[0].ycor() > 395 or snake.snake_parts[0].ycor() < -395:
        game_is_on = False
        scoreboard.game_over()
        
    # Detect collision with tail
    for snake_part in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(snake_part) < 5:
            game_is_on = False
            scoreboard.game_over()
        
    








screen.exitonclick()