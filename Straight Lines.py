# This program makes a circle with all straight lines
# Alexander Parker 2016

from turtle import *
from random import randint
from math import *

#Variables
sides = 500 #sides
side_length = 3 #pixels
screen_size = 512 #pixels
speed(0) #speed from 1 (slowest) to 10 (fastest)
hideturtle() # hideturtle() or showturtle()

#Constants
angle = 360.0 / sides
coords = []
x = 0
n = 0

# Function Definitions
def redIntensity(ratio):
	a = int((255*cos(2*pi*ratio)+127))
	if a > 255:
		return 255
	elif a < 0:
		return 0
	return a

def greenIntensity(ratio):
	a = int((255*cos(2*pi*ratio - (2*pi)/3)+127))
	if a > 255:
		return 255
	elif a < 0:
		return 0
	return a
	
def blueIntensity(ratio):
	a = int((255*cos(2*pi*ratio - (4*pi)/3)+127))
	if a > 255:
		return 255
	elif a < 0:
		return 0
	return a

# Set up the screen
setup(1366, 768)
title('Straight Lines')
colormode(255)
bgcolor(255, 255, 255)

#Start more centred
penup()
goto(0, (screen_size / 2))
pendown()

#Draw the polygon
tracer(0)
for i in range(sides):
    forward(side_length)
    coords.append(pos()) #Save co-ordinates of all corners
    right(angle)
tracer(1)

coordLength = len(coords)
totalLines = float(coordLength * (sides - 5))
colourCounter = 0

tracer(0)

#Draw the lines
for i in range(sides):
    for i in range(len(coords)):
        penup()
        r = redIntensity(colourCounter/totalLines)
        g = greenIntensity(colourCounter/totalLines)
        b = blueIntensity(colourCounter/totalLines)
        pencolor((r, g, b))
        goto(coords[x])
        pendown()           
        goto(coords[n])
        n = n + 1
        colourCounter += 1	

    n = 0
    coords.remove(coords[0])
    x = x
tracer(1)

done() #release the drawing window