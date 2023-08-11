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
simLen = [1,0]    # Simulation length - [yrs,days]
music = "4"
musicFiles =["track1.mp3", "track2.mp3", "track3.mp3", None]


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
                showPlanetsPage(screen,backgroundColor,days,functionNames,distance)

            elif newPlanet.isOver(pos):
                function, funcName = newPlanetPage(screen,backgroundColor)
                functions.append(function)
                functionNames.append(funcName)
                
                day, dist = daysPage(screen,backgroundColor)
                days.append(day)
                distance.append(dist)

            elif delete.isOver(pos):
                deleteIndex = deletePage(screen,backgroundColor,days,functionNames,distance)
                if deleteIndex != None:
                    days.pop(deleteIndex-1)
                    distance.pop(deleteIndex)
                    functions.pop(deleteIndex)
                    functionNames.pop(deleteIndex-1)
                
            elif draw.isOver(pos):
                from Drawing_Solar_System import *
                length = int((simLen[0]*36)+((round(simLen[1]+10))/10))
                drawSolarSystem(functions,days,distance,length)
                
            elif settings.isOver(pos):
                simLen,music = settingsPage(screen,backgroundColor,simLen,music)
                ## play music
                if int(music) < 4:                                        
                    mixer.music.load(musicFiles[int(music)-1])
                    mixer.music.play(-1)
                else:
                    mixer.music.stop() 
    
        ## updating screen
        pygame.display.update()


