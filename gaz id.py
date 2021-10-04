from random import randint
import turtle
turtle.mode("standard")
number_of_turtles = 20
turtle.penup()
turtle.forward(400)
turtle.pendown()
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)

turtle.goto(400, -300)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
circle = 0
while circle < 20:
    pool[circle].penup()
    pool[circle].goto(randint(-200, 200), randint(-200, 200))
    pool[circle].right(randint(0, 360))
    circle += 1

while True:
    k = 0
    while k < 20:
        if pool[k].xcor() < -400:
            a = pool[k].heading()
            pool[k].goto(-395, pool[k].ycor())
            pool[k].right(2*(a-90))

        if pool[k].xcor() > 400:
            b = pool[k].heading()
            pool[k].goto(395, pool[k].ycor())
            pool[k].left(2 * (90-b))
        if pool[k].ycor() > 300:
            c = pool[k].heading()
            pool[k].goto(pool[k].xcor(), 295)
            pool[k].right(2 * c)
        if pool[k].ycor() < -300:
            d = pool[k].heading()
            pool[k].goto(pool[k].xcor(), -295)
            pool[k].left(2 * (360 - d))
        pool[k].forward(3)
        k += 1
