import turtle, time
from Challenge_3_Drawing_Planets_Functions_Animation import *

### BASIC VARIABLES ###

# holds distance of planets from sun in miles 
distance =[0,3.598e7,6.724e7,9.296e7,1.416e8]
# radius of each planet in miles, starting with sun
radius =[432690,1516,3760.4,3958.8,2106.1]
# functions to draw each planet
functions = [sun,mercury,venus,earth,mars]
# pens
planetPens = [sunPen,mercuryPen,venusPen,earthPen,marsPen]
orbitPens =  [sunOrbitPen,mercuryOrbitPen,venusOrbitPen,earthOrbitPen,marsOrbitPen]

### SET UP SCREEN ###

screen = turtle.Screen()
screen.bgcolor("#000000") # color screen black

functions[0](0,0,planetPens[0]) # draw sun

for pen in orbitPens:
    ## set all pen colors as white
    pen.pencolor("#ffffff")
    ## hide all pens
    pen.hideturtle()
    
for pen in planetPens:
    ## hide all pens
    pen.hideturtle()

screen.tracer(0)


## set starting position & distance from sun for drawing orbits
for i in range(1,5):
    orbitPens[i].penup()
    orbitPens[i].forward(distance[i]/8e5)
    orbitPens[i].setheading(90)
    orbitPens[i].pendown()

## Animation
while True:

    for i in range(1,5):
        ## draw orbit
        orbitPens[i].circle(distance[i]/8e5,10)

        ## clear old planet
        planetPens[i].clear()
        ## draw planet in new position
        functions[i](orbitPens[i].xcor(),orbitPens[i].ycor(),planetPens[i])

    ## update screen and pause
    screen.update()
    time.sleep(0.1)
    

    



