import time
import turtle
turtle.speed(0)
turtle.hideturtle()
turtle.up()
tm = time.localtime()
turtle.goto(0, -50)
turtle.write(f'{tm.tm_mon}/{tm.tm_mday}/{tm.tm_year}', align='center', font=('Arial', 50, 'normal'))
turtle.goto(0, 50)
a = time.time()
while True:
    tm = time.localtime()
    turtle.write(f'{tm.tm_hour} : {tm.tm_min} : {tm.tm_sec}', align='center', font=('Arial', 50, 'normal'))
    turtle.undo()
