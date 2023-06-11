import turtle
from Challenge_2_Drawing_Planets_Functions import *

### BASIC VARIABLES ###

# holds distance of planets from sun in miles 
distance =[0,3.598e7,6.724e7,9.296e7,1.416e8,4.838e8,8.909e8,1.784e9,2.793e9]
# radius of each planet in miles, starting with sun
radius =[432690,1516,3760.4,3958.8,2106.1,43441,36184,15759,15299]
# functions to draw each planet
functions = [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
# pens
pens = [sunPen,mercuryPen,venusPen,earthPen,marsPen,jupiterPen,saturnPen,uranusPen,neptunePen]
