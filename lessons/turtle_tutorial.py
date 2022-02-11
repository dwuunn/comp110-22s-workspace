from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.speed(50)

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

leo.hideturtle()

done()