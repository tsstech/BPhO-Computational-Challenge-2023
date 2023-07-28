import pygame, sys
from pygame import mixer
from Drawing_Planets_Functions import *
from Create_a_Solar_System_Functions import *
 
# Initialize program
pygame.init()
 
# create screen
screen = pygame.display.set_mode((800,600))

# title & icon
pygame.display.set_caption("Create a Solar System")        # displaying title
##############icon = pygame.image.load('space-invaders-logo.png') # variable to hold logo
##############pygame.display.set_icon(icon)                       # displaying logo

# background
#background = pygame.image.load('background.png')

# background music
#mixer.music.load("background-music.mp3")
#mixer.music.play(-1)



## defining text buttons for homepage
font = pygame.font.Font("FredokaOne-Regular.ttf", 30)  

newPlanet = TextButton(245, 180, 320, 50, ("#84A7BA"), text="New Planet")
showPlanets = TextButton(245, 240, 320, 50, ("#84A7BA"), text="Show My Planets")
delete = TextButton(245, 300, 320, 50, ("#84A7BA"), text="Delete Planet")
draw = TextButton(245, 360, 320, 50, ("#84A7BA"), text="Draw Solar System")
settings = TextButton(245, 420, 320, 50, ("#84A7BA"), text="Settings")


######## BASIC VARIABLES #######
backgroundColor = "#303655"
titleFont = pygame.font.Font('FredokaOne-Regular.ttf',50)


######## VARIABLES FOR TURTLE ########
functions = [sun]
functionNames =[]
days = []
distance = [0]


# game loop
running = True
        
while running:

    # screen background color
    screen.fill(backgroundColor)

    ## title
    title = titleFont.render("Create a Solar System!",True,(255,255,255))
    screen.blit(title,(125,60))

    ## drawing buttons
    newPlanet.draw(screen)
    showPlanets.draw(screen)
    draw.draw(screen)
    delete.draw(screen)
    settings.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if showPlanets.isOver(pos):
                showPlanetsPage(screen,days,functionNames,distance)

            elif newPlanet.isOver(pos):
                function, funcName = newPlanetPage(screen)
                functions.append(function)
                functionNames.append(funcName)
                
                day, dist = daysPage(screen)
                days.append(day)
                distance.append(dist)

            elif delete.isOver(pos):
                deleteIndex = deletePage(screen,days,functionNames,distance)
                if deleteIndex != None:
                    days.pop(deleteIndex-1)
                    distance.pop(deleteIndex)
                    functions.pop(deleteIndex)
                    functionNames.pop(deleteIndex-1)
                
            elif draw.isOver(pos):
                from Drawing_Solar_System import *
                drawSolarSystem(functions,days,distance)

            
                
    
    ## updating screen
    pygame.display.update()


