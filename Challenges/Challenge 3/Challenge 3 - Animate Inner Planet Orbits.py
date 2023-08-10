import turtle, time
from planet_icon_functions import *

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
speed = [0,40,16,10,6.2]

### SET UP SCREEN ###

screen = turtle.Screen()
screen.bgcolor("#000000") # color screen black

functions[0](-10,0,planetPens[0]) # draw sun
planetPens[0].hideturtle()


### SET UP PENS ###
for pen in orbitPens:
    ## set all pen colors as white
    pen.pencolor("#ffffff")
    ## hide all pens
    pen.hideturtle()
    
for pen in planetPens:
    ## hide all pens
    pen.hideturtle()

## writing pen
turtle.pencolor("#ffffff")
turtle.penup()
turtle.setpos(-230,230)
turtle.pendown()

## animaton setup
screen.tracer(0)
t = 0


## set starting position & distance from sun for drawing orbits
for i in range(1,5):
    orbitPens[i].penup()
    orbitPens[i].forward(distance[i]/8e5)
    orbitPens[i].setheading(90)
    orbitPens[i].pendown()

## Animation
while True:

    ## write time
    t += 10
    turtle.clear()
    if t > 360:
        if t % 360 == 0:
            turtle.write(f"Time = {t//360} years", font=("Verdana", 15, "normal"))
        else:
            turtle.write(f"Time = {t//360} years {t%360} days", font=("Verdana", 15, "normal"))
    else:
        turtle.write(f"Time = {t} days", font=("Verdana", 15, "normal"))

    
    for i in range(1,5):
        ## draw orbit
        orbitPens[i].circle(distance[i]/8e5,speed[i])

        ## clear old planet
        planetPens[i].clear()
        ## draw planet in new position
        functions[i](orbitPens[i].xcor(),orbitPens[i].ycor(),planetPens[i])

    ## update screen and pause
    screen.update()
    time.sleep(0.1)
    

    



