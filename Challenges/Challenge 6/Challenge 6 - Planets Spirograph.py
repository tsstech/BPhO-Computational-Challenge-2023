import turtle, time
from planet_icon_functions import *

### BASIC VARIABLES ###

# holds distance of planets from sun in miles 
distance = {"mercury" : 3.598e7,
                  "venus" : 6.724e7,
                  "earth" : 9.296e7,
                  "mars" : 1.416e8}

# radius of each planet in miles, starting with sun
radius = {"mercury" : 1516,
               "venus" : 3760.4,
               "earth" : 3958.8,
               "mars" : 2106.1}

# functions to draw each planet
functions = {"mercury" : mercury,
                   "venus" : venus,
                   "earth" : earth,
                   "mars" : mars}

# pens
drawPen = turtle.Turtle()
drawDistance = 10 ## distance for when to draw lines, connecting orbit
planetPens = [turtle.Turtle(),turtle.Turtle()]
orbitPens =  [turtle.Turtle(),turtle.Turtle()]
speed = {"mercury" : 40,
               "venus" : 16,
               "earth" : 10,
               "mars" : 6.2}



### SET UP SCREEN ###

screen = turtle.Screen()
screen.bgcolor("#000000") # color screen black



### SET UP PENS ###
for pen in orbitPens:
    ## set all pen colors as blue
    pen.pencolor("#00b8ff")
    ## hide all pens
    pen.hideturtle()
    
for pen in planetPens:
    ## hide all pens
    pen.hideturtle()

drawPen.color("#ffffff")
drawPen.hideturtle()

## writing pen
turtle.pencolor("#ffffff")
turtle.penup()
turtle.setpos(-230,230)
turtle.pendown()

## animaton setup
screen.tracer(0)
t = 0


## Input Planets
planets = [input("Choose a planet: ").lower(), input("Choose another planet: ").lower()]


## set starting position & distance from sun for drawing orbits
for i in range(2):
    orbitPens[i].penup()
    orbitPens[i].forward(distance[f"{planets[i]}"]/8e5)
    orbitPens[i].setheading(90)
    orbitPens[i].pendown()




## Animation
iterations = 0
while True:

    ## draw pattern
    if iterations % drawDistance == 0:
        drawPen.penup()
        drawPen.setpos(orbitPens[0].xcor(),orbitPens[0].ycor())
        drawPen.pendown()
        drawPen.setpos(orbitPens[1].xcor(),orbitPens[1].ycor())

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
    for i in range(2):
        ## draw orbit
        orbitPens[i].circle(distance[f"{planets[i]}"]/8e5,speed[f"{planets[i]}"])

        ## clear old planet
        planetPens[i].clear()
        ## draw planet in new position
        functions[f"{planets[i]}"](orbitPens[i].xcor(),orbitPens[i].ycor(),planetPens[i])

    ## update screen and pause
    screen.update()
    time.sleep(0.1)
    

    



