import turtle
turtle.speed(10)
turtle.hideturtle()
for i in range(361):
    if i % 120 == 0:
        turtle.width(5)
        turtle.pendown()
        turtle.setx(i)
        turtle.left(90)
        turtle.fd(360)
        turtle.penup()
        turtle.home()
    elif i % 40 == 0:
        turtle.width(3)
        turtle.pendown()
        turtle.setx(i)
        turtle.left(90)
        turtle.fd(360)
        turtle.penup()
        turtle.home()
for j in range(361):
    if j % 120 == 0:
        turtle.width(5)
        turtle.pendown()
        turtle.sety(j)
        turtle.right(0)
        turtle.fd(360)
        turtle.penup()
        turtle.home()
    if j % 40 == 0:
        turtle.width(3)
        turtle.pendown()
        turtle.sety(j)
        turtle.right(0)
        turtle.fd(360)
        turtle.penup()
        turtle.home()
