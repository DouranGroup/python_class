import time
import datetime as dt
import turtle

turtle.title("Age ino khondi salavat khatm kon")
t = turtle.Turtle()
t1 = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("magenta")

sec = dt.datetime.now().second
dagh = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(3)
t1.color('black')
t1.penup()

t1.goto(-100, 0)
t1.pendown()

for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

t1.hideturtle()

while True:
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-78, -1)
    t.pendown()
    t.write(f"{str(hr).zfill(2)}:{str(dagh).zfill(2)}:{str(sec).zfill(2)}",
            font=("Calibri", 35, "bold"))
    time.sleep(1)
    sec += 1

    if sec == 60:
        sec = 0
        dagh += 1
    if dagh == 60:
        dagh = 0
        hr += 1
    if hr == 13:
        hr = 1
