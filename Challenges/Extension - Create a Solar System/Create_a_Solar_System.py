import pygame, sys
from pygame import mixer
from Drawing_Planets_Functions import *
 
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




############### BUTTONS #################

## TEXT button class 
class TextButton(object):
    def __init__(self, x, y, width, height, colour1, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour1 = colour1
        self.text = text
        
    def draw(self, screen):  # draws centralised buttons and text
        text = font.render(self.text, 1, (255,255,255))
        pygame.draw.rect(screen, self.colour1,
                         (self.x, self.y, self.width, self.height),0)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):  # detects if mouse positions is above buttons'
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


## IMAGE button class
class ImageButton(object):
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        
    def draw(self, screen):  # draws centralised buttons and text
        screen.blit(self.image, (self.x, self.y))

    def isOver(self, pos):  # detects if mouse positions is above buttons'
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    


## defining text buttons for homepage
font = pygame.font.Font("FredokaOne-Regular.ttf", 30)  

showPlanets = TextButton(245, 200, 320, 50, ("#84A7BA"), text="Show My Planets")
newPlanet = TextButton(300, 300, 210, 50, ("#84A7BA"), text="New Planet")
draw = TextButton(245, 400, 320, 50, ("#84A7BA"), text="Draw Solar System")
settings = TextButton(345, 500, 320, 50, ("#84A7BA"), text="Settings")


######## BASIC VARIABLES #######
backgroundColor = "#303655"


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

    ## drawing buttons
    showPlanets.draw(screen)
    newPlanet.draw(screen)
    draw.draw(screen)
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

            elif draw.isOver(pos):
                from Drawing_Solar_System import *
                drawSolarSystem(functions,days,distance)
                
    
    ## updating screen
    pygame.display.update()


