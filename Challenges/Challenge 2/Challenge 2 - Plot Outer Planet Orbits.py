import turtle
from planet_icon_functions import *

### DECLARE BASIC LIST VARIABLES ###

# holds distance of planets from sun in miles 
distance =[0,3.598e7,6.724e7,9.296e7,1.416e8,4.838e8,8.909e8,1.784e9,2.793e9]
# radius of each planet in miles, starting with sun
radius =[432690,1516,3760.4,3958.8,2106.1,43441,36184,15759,15299]
# functions to draw each planet
functions = [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
# pens
pens = [sunPen,mercuryPen,venusPen,earthPen,marsPen,jupiterPen,saturnPen,uranusPen,neptunePen]


## Screen Setup
turtle.bgcolor("#000000") # color screen black


for pen in pens:
    ## set all pen colors as white
    pen.pencolor("#ffffff")
    ## hide all pens
    pen.hideturtle()



##### DRAW ORBITS #####
## loop through lists
for i in range(1,9):
    ## set position to draw orbit
    pens[i].penup()
    pens[i].forward(distance[i]/9.9e6)
    pens[i].setheading(90)
    pens[i].pendown()
    ## draw orbit
    pens[i].circle(distance[i]/9.9e6)
    ## if its an outer planet, draw the planet
    if i > 4:
        functions[i](pens[i].xcor(),pens[i].ycor(),pens[i])

    



