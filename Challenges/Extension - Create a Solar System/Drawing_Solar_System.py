import turtle, time
from Drawing_Planets_Functions import *


def drawSolarSystem(functions,days,distance,simLen):
    ### BASIC VARIABLES ###

    # functions to draw each planet
    functions = functions
    # pens
    planetPens = [turtle.Turtle() for i in range(len(functions))]
    orbitPens =  [turtle.Turtle() for i in range(len(functions))]

    # orbit length of each planet in earth days, starting with mercury
    days = days
    speed = [3600/days[i] for i in range(len(days))]
    # holds distance of planets from sun in miles 
    distance = distance

    ### SET UP SCREEN ###

    screen = turtle.Screen()
    screen.bgcolor("#000000") # color screen black

    functions[0](0,0,planetPens[0]) # draw sun
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
    iterations = 0


    ## set starting position & distance from sun for drawing orbits
    for i in range(1,len(orbitPens)):
        orbitPens[i].penup()
        orbitPens[i].forward(distance[i]/8e5)
        orbitPens[i].setheading(90)
        orbitPens[i].pendown()

    ## Animation
    for i in range(simLen):

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

        
        for i in range(1,len(orbitPens)):
            ## draw orbit
            orbitPens[i].circle(distance[i]/8e5,speed[i-1])

            ## clear old planet
            planetPens[i].clear()
            ## draw planet in new position
            degrees = speed[i-1]*iterations
            functions[i](orbitPens[i].xcor(),orbitPens[i].ycor(),planetPens[i],degrees)

        ## update screen and pause
        screen.update()
        time.sleep(0.1)

    screen.exitonclick()
