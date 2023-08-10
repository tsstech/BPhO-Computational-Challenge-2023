import turtle
turtle.bgcolor("#000000")

def sun(x,y,pen):
    # setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+10,y)
    pen.left(90)
    pen.pendown()
    # setting pen colors
    pen.pencolor("#fcba03")
    pen.fillcolor("#fcba03")
    # drawing sun
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()

def mercury(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+3,y)
    pen.pendown()
    # setting pen colors
    pen.pencolor("#dbd8d0")
    pen.fillcolor("#dbd8d0")
    # drawing planet
    pen.begin_fill()
    pen.circle(3)
    pen.end_fill()

def venus(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+7,y)
    pen.pendown()
    # setting pen colors
    pen.pencolor("#f09e07")
    pen.fillcolor("#f09e07")
    # drawing planet
    pen.begin_fill()
    pen.circle(7)
    pen.end_fill()

def earth(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+7,y)
    pen.pendown()
    # setting pen colors
    pen.pencolor("#133e9c")
    pen.fillcolor("#133e9c")
    # drawing planet
    pen.begin_fill()
    pen.circle(7)
    pen.end_fill()
    # setting colors for land detail
    pen.pencolor("#72ff6b")
    pen.fillcolor("#72ff6b")
    # drawing land detail onto planet
    pen.begin_fill()
    pen.left(125)
    pen.forward(5)
    pen.right(60)
    pen.forward(4)
    pen.right(25)
    pen.forward(2)
    pen.right(70)
    pen.forward(3)
    pen.left(20)
    pen.forward(5)
    pen.penup()
    pen.setpos(x+7,y)
    pen.pendown()
    pen.left(5)
    pen.circle(7,90)
    pen.end_fill()

def mars(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+5,y)
    pen.pendown()
    # setting pen colors
    pen.pencolor("#ff171f")
    pen.fillcolor("#ff171f")
    # drawing planet
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

def jupiter(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+10,y)
    pen.pendown()
    # setting pen colors & width
    pen.width(1)
    pen.pencolor("#c78454")
    pen.fillcolor("#c78454")
    # drawing planet
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    # drawing detail on planet
    pen.width(2)
    pen.pencolor("#cf9a74")
    pen.left(90)
    pen.forward(19)

    pen.width(1)
    pen.pencolor("#edc09f")
    pen.penup()
    pen.right(90)
    pen.forward(4)
    pen.right(90)
    pen.forward(1)
    pen.pendown()
    pen.forward(19)

    pen.width(3)
    pen.pencolor("#6e3409")
    pen.penup()
    pen.setpos(x,y-4)
    pen.pendown()
    pen.forward(2)

def saturn(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+9,y)
    pen.pendown()
    # setting pen colors & width
    pen.width(1)
    pen.pencolor("#d69b6f")
    pen.fillcolor("#d69b6f")
    # drawing planet
    pen.begin_fill()
    pen.circle(9)
    pen.end_fill()
    
    # setting up to draw ring
    pen.width(2)
    pen.color("#824416")
    pen.penup()
    pen.setpos(x+9,y+4)
    pen.pendown()
    pen.right(90)
    # drawing ring
    pen.forward(2)
    for i in range(10):
        pen.right(18)
        pen.forward(0.8)
    pen.forward(20)
    for i in range(10):
        pen.right(18)
        pen.forward(0.8)

def uranus(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+7,y)
    pen.pendown()
    # setting pen colors
    pen.pencolor("#afe0f0")
    pen.fillcolor("#afe0f0")
    # drawing planet
    pen.begin_fill()
    pen.circle(7)
    pen.end_fill()

def neptune(x,y,pen):
    #setting starting position
    pen.hideturtle()
    pen.penup()
    pen.setpos(x+6,y)
    pen.pendown()
    # setting pen colors
    pen.pencolor("#184a87")
    pen.fillcolor("#184a87")
    # drawing planet
    pen.begin_fill()
    pen.circle(6)
    pen.end_fill()


sunPen = turtle.Turtle()
mercuryPen = turtle.Turtle()
venusPen = turtle.Turtle()
earthPen = turtle.Turtle()
marsPen = turtle.Turtle()
jupiterPen = turtle.Turtle()
saturnPen = turtle.Turtle()
uranusPen = turtle.Turtle()
neptunePen = turtle.Turtle()

