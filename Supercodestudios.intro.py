import time
from turtle import *
import turtle
from itertools import cycle
wn = turtle.Screen()
wn.title("Snake Game by SuperCodeStudios")
def draw_circle(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
color('blue', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
turtle.penup()
turtle.goto (-250, -30)
turtle.pendown()
turtle.write("SuperCodeStudios", font=("Verdana",
                                    25, "normal"))
turtle.hideturtle()
time.sleep(5)
turtle.clearscreen()
