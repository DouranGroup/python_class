import turtle

turtle.hideturtle()
turtle.penup()
turtle.speed(-1)
turtle.goto(-200, 200)
turtle.pensize(5)
turtle.pendown()
for i in range(4):
    turtle.forward(450)
    turtle.right(90)

turtle.pensize(3)
turtle.forward(150)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.pensize(1)
turtle.forward(450)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(450)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(450)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(450)

turtle.penup()
def fill_number(num, row, col):
    turtle.goto(col * 50 - 175, 150 - row * 50)
    turtle.write(num, font=("Arial", 30, "normal"))


fill_number(7, 0, 0)
fill_number(8, 0, 1)
fill_number(5, 0, 4)
fill_number(9, 1, 0)
fill_number(3, 1, 3)
fill_number(4, 1, 4)
fill_number(6, 2, 1)
fill_number(8, 2, 2)
fill_number(2, 2, 3)
fill_number(7, 3, 3)
fill_number(8, 3, 4)
fill_number(5, 3, 5)
fill_number(9, 3, 6)
fill_number(3, 3, 7)
fill_number(4, 3, 8)
fill_number(6, 3, 0)
fill_number(8, 3, 2)
fill_number(2, 5, 5)
fill_number(1, 7, 8)
fill_number(2, 5, 6)
fill_number(3, 4, 5)
fill_number(4, 5, 4)
fill_number(5, 6, 2)
fill_number(6, 5, 8)
fill_number(7, 6, 7)
fill_number(8, 7, 6)
fill_number(9, 8, 5)
fill_number(1, 8, 7)
fill_number(8, 2, 8)
fill_number(3, 7, 7)
fill_number(9, 4, 7)
fill_number(2, 5, 6)
fill_number(4, 6, 6)
fill_number(6, 7, 5)
fill_number(8, 6, 5)
fill_number(2, 7, 4)
fill_number(1, 8, 0)
fill_number(8, 6, 1)
fill_number(5, 7, 0)
fill_number(9, 0, 8)
fill_number(3, 1, 7)
fill_number(4, 2, 6)
fill_number(6, 5, 0)
# fill_number(8, 2, 2)
# fill_number(2, 2, 3)

turtle.done()
