import turtle
import time

t1 = turtle.Turtle()
t2 = turtle.Turtle()



# turtle.tracer(0)
turtle.mode('logo')
turtle.dot(5)
turtle.hideturtle()
turtle.speed(0)
turtle.up()
turtle.goto(0, -200)
turtle.right(90)
for i in range(60):
    turtle.right(90)
    turtle.down()
    if i % 5 == 0:
        turtle.pensize(5)
        turtle.fd(10)
        turtle.bk(10)
    else:
        turtle.pensize(1)
        turtle.fd(3)
        turtle.bk(3)
    turtle.left(90)
    turtle.up()
    turtle.circle(200, 6)
turtle.home()
turtle.down()
while True:
    tm = time.localtime()
    turtle.pensize(5)
    turtle.setheading(((tm.tm_hour % 12) * 30) + (tm.tm_min / 2))
    turtle.fd(100)
    turtle.home()
    turtle.setheading((tm.tm_min * 6) + (tm.tm_sec / 10))
    turtle.fd(150)
    turtle.home()
    turtle.pensize(1)
    turtle.setheading(tm.tm_sec * 6)
    turtle.fd(150)
    turtle.home()
    time.sleep(0.98)
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()

    
    