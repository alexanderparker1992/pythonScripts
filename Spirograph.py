# This is a program to draw a spirograph using turtle
# Alexander Parker 2017

from turtle import *
from random import randint

# Variables
screen_size = 768 #pixels
lines = 20 #number of lines to draw per side
speed(0) #speed from 1 (slowest) to 10 (fastest)
showturtle() # hideturtle() or showturtle()
colormode(255)
variation = 15
gap = 15

# Set up the screen
setup(screen_size, screen_size)
title('Spirograph')
bgcolor("white")

# Define the square corners
top_right =((screen_size / 4), (screen_size / 4))
bottom_right =((screen_size / 4), -(screen_size / 4))
top_left =(-(screen_size / 4), (screen_size / 4))
bottom_left =(-(screen_size / 4), -(screen_size / 4))

# Start at the corner
penup()
goto(top_right)
right(90) # Orient the right way
pendown()

# Evenly divide the square into segments
line_segments = range(((lines * 2) -2) + 1)

# Define distances between the grids
grid_distance = (screen_size/4) / (lines)

coords = [] # Make a list of co-ordinates

# Draw square and save list of co-ordinates
for square in range(4):
    for grid in line_segments:
        forward(grid_distance)
        coords.append(pos())

    forward(grid_distance)
    right(90)
    
# Go to the corner
penup()
goto((screen_size / 4), (screen_size / 4))
pendown()

# Draw a line starting from the first co-ordinate to the corresponding co-ordinate
# on the appropriate line.
# the next function calls for n+1. Start at -1
# to start at first item in list [0]
n = -1

# Define random starting colours
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

for pattern in range((len(coords)) / 4):
    pencolor((r, g, b))
    goto(coords[n + 1])
    goto(coords[((lines * 4) + 1)])
    n = n + 1
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)

done() # Release the drawing window