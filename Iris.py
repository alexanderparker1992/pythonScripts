# This is a program to make an iris of different sizes
# Alexander Parker 2017

from turtle import *
from random import randint
from math import *
from time import *

# Variables
sides = 250 #sides
side_length = 10 #pixels
speed(0) #speed from 1 (slowest) to 10 (fastest)
hideturtle() # hideturtle() or showturtle()
screen_height = 768 #pixels
screen_width = 1366 #pixels
offset = 1
pensize(1)

# Constants
angle = 360.0 / sides
cords = []
x = 0
n = 0

# Set up the screen
setup(screen_width, screen_height)
title('Iris')
colormode(255)
bgcolor(255, 255, 255)

# Start more centred
penup()
goto(0, (screen_height / 2.5))
pendown()

tracer(0)
# Draw the polygon
for i in range(sides):
    forward(side_length)
    cords.append(pos()) #Save co-ordinates of all corners
    right(angle)
tracer(1)

# Draw the lines
penup()
goto(cords[0])
pendown()
for i in range(sides / 2 - 1):
    tracer(0)
    #pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    for i in range(sides + 1):
        goto(cords[n])
        n = n + offset
        if n >= (len(cords)):
            n = n - len(cords)
    offset = offset + 1
    sleep(.2)
    tracer(1)
for i in range(cords - 1):
    cords.pop()

done() #release the drawing window