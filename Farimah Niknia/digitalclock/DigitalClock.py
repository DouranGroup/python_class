import time
import datetime
import turtle

turtle.tracer(0)

t2 = turtle.Turtle()
t2.hideturtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(-100, 70)
turtle.pendown()
turtle.pensize(6)
turtle.color('pink')
turtle.speed(100)
for i in range(2):
    turtle.forward(185)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
local = time.localtime()
hour = local.tm_hour
mnt = local.tm_min
sec = local.tm_sec
while True:
    t2.penup()
    t2.goto(-85, 0)
    t2.clear()
    t2.pendown()
    t2.write(str(hour).zfill(2) + ':' + str(mnt).zfill(2) + ':' + str(sec).zfill(2), font=('Time New Roman', 37, 'bold'))
    time.sleep(1)
    sec = sec + 1
    if sec == 60:
        sec = 0
        mnt = mnt + 1
    if mnt == 60:
        mnt = 0
        hour = hour + 1
    if hour == 13:
        hour = 1
