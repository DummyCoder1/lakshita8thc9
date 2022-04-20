import turtle

import turtle

import random, turtle
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
colours = ['red', 'green', 'blue', 'pink', 'yellow']

def lines(l, c):
    for i in l:
        turtle.forward(i)
        turtle.pencolor(random.choice(c))
        (turtle.stamp())
        turtle.backward(i)
        turtle.left(30)
lines(list,colours)