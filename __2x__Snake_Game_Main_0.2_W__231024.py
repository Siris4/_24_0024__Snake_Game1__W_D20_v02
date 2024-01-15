import turtle
from turtle import Turtle, Screen

# game_on = False

snake = Turtle()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
turtle.title("Siris's Snake Game")    #lables the Title of the pop-up window!

starting_positions = [(0, 0), (-20, 0), (-40, 0)]    #will ALWAYS start here, so using Tuples is PERFECT!!
snake_segments = []

# TODO 1: Create the Snake Body
# 3 squares, which are going to be turtles

# x_coords = 0
# y_coords = 0

for snake_block_body_loop_iteration in starting_positions:
    body__individual_snake_block = Turtle(shape="square")
    snake.pensize(20)
    body__individual_snake_block.color("white")
    body__individual_snake_block.goto(snake_block_body_loop_iteration)
    # x_coords -= 20
    snake_segments.append(body__individual_snake_block)  # up un

game_on = True

while game_on:
    for segment in snake_segments:
        snake.forward(20)





















screen.exitonclick()