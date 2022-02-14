"""Ex04: practice turtle, sketch a night scene."""

__author__ = "730393353"

from turtle import Turtle, colormode, done 
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    skyscraper: Turtle = Turtle()
    skyscraper.speed(0)
    draw_rec(skyscraper, 20, 300, 200, 500)
    draw_tri(skyscraper, 20, 300, 200)
    draw_square(skyscraper, 40, 50, 60)
    draw_square(skyscraper, 40, 160, 60)
    draw_square(skyscraper, 40, 270, 60)
    draw_square(skyscraper, 140, 50, 60)
    draw_square(skyscraper, 140, 50, 60)
    draw_square(skyscraper, 140, 160, 60)
    draw_square(skyscraper, 140, 270, 60)

    sky: Turtle = Turtle()
    sky.speed(0)
    d: int = -300
    while d < 30: 
        draw_star(sky, d, 300, 20)
        d += 30

    moon: Turtle = Turtle()
    """Draw a full moon."""
    moon.penup()
    moon.goto(-500, 300)
    moon.setheading(0.0)
    moon.fillcolor("yellow")
    moon.shape("circle")
    moon.shapesize(6, 6)
    moon.pendown()

    done()


# TODO: Define the procedures for other components in your scene here.
def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.color(85, 116, 202)
    a_turtle.fillcolor(85, 116, 202)
    a_turtle.pendown()
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


def draw_rec(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of the given length and width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(length)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(length)
    a_turtle.right(90)
    a_turtle.hideturtle()


def draw_tri(a_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Draw a equilateral triangle."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 3:
        a_turtle.forward(length)
        a_turtle.left(120)
        i += 1
    a_turtle.hideturtle()


def draw_star(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Draw a star."""
    a_turtle.fillcolor("yellow")
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.begin_fill()
    i: int = 0
    while i < 5:
        a_turtle.left(144)
        a_turtle.forward(size)
        i += 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


if __name__ == "__main__":
    main()