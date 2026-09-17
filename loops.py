import turtle
from turtle import *
t = Turtle()
t.speed(1000)

def Square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)
# Square(100)

def Triangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)
# Triangle(200)

def Square(x):
    for i in range(60):
        for i in range(4):
            t.forward(x)
            t.left(90)
        t.right(5)
# Square(200)

length = 5
for i in range(60):
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.right(5)
    length += 5

turtle.done()