import turtle
turtle.goto(0, 0)
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.setx(60)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(70)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.setx(140)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(90)
    turtle.right(144)
turtle.end_fill()