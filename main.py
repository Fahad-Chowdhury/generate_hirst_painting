from turtle import Turtle, Screen
from random import choice
from image_colors import selected_colors


def generate_hirst_painting(height, width):
    """ Generate a hirst painting of dots of random color selected from
    'selected_colors' and of size od height and width. """
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)
    x, y = -250, -250
    for _ in range(height):
        for _ in range(width):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.dot(20, choice(selected_colors))
            x += 50
        x = -250
        y += 50


def main():
    """ Main method to generate the painting. """
    my_screen = Screen()
    my_screen.colormode(255)
    generate_hirst_painting(10, 10)
    print('Click on screen to close the drawing.')
    my_screen.exitonclick()


if __name__ == "__main__":
    main()
