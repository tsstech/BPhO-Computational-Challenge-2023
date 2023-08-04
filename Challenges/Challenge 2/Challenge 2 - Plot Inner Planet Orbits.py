import turtle
from Challenge_2_Drawing_Planets_Functions import *

### BASIC VARIABLES ###

# holds distance of planets from sun in miles 
distance =[0,3.598e7,6.724e7,9.296e7,1.416e8]
# radius of each planet in miles, starting with sun
radius =[432690,1516,3760.4,3958.8,2106.1]
# functions to draw each planet
functions = [sun,mercury,venus,earth,mars]
# pens
pens = [sunPen,mercuryPen,venusPen,earthPen,marsPen]


turtle.bgcolor("#000000") # color screen black

functions[0](-10,0,pens[0]) # draw sun

for pen in pens:
    ## set all pen colors as white
    pen.pencolor("#ffffff")
    ## hide all pens
    pen.hideturtle()

##draw the orbits
for i in range(1,5):
    ## set position for drawing orbit
    pens[i].penup()
    pens[i].forward(distance[i]/8e5)
    pens[i].setheading(90)
    pens[i].pendown()
    ## draw orbit
    pens[i].circle(distance[i]/8e5)
    ## draw planet
    functions[i](pens[i].xcor(),pens[i].ycor(),pens[i])

    



