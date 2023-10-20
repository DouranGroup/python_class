import turtle
import random

turtle.tracer(0)
choices = (1, 2, 3, 4, 5, 6, 7, 8, 9)
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(5)
turtle.up()
turtle.goto(-180, -180)
turtle.down()
for i in range(4):
    turtle.fd(360)
    turtle.left(90)
turtle.pensize(3)
for j in range(4):
    turtle.fd(120)
    turtle.left(90)
    turtle.fd(360)
    turtle.left(90)
    turtle.fd(120)
    turtle.left(90)
turtle.pensize(1)
for k in range(6):
    turtle.fd(40)
    turtle.left(90)
    turtle.fd(360)
    turtle.right(90)
    turtle.fd(40)
    turtle.right(90)
    turtle.fd(360)
    turtle.left(90)
    turtle.fd(40)
    if k == 2:
        turtle.left(90)
turtle.right(90)
turtle.up()
turtle.goto(-180, -180)
turtle.bk(3)
for r in range(9):
    for g in range(9):
        a = random.choice(choices)
        turtle.write(f' {a} ', True, font=('verdana', 23, 'normal'))
    turtle.bk(369)
    turtle.left(90)
    turtle.fd(40)
    turtle.right(90)

turtle.done()
