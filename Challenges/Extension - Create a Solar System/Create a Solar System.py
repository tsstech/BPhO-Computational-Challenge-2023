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
    

## defining text buttons
font = pygame.font.SysFont('comicsans', 30, True)  

newPlanet = TextButton(300, 300, 210, 50, (172,146,237), text="New Planet")
draw = TextButton(245, 400, 320, 50, (172,146,237), text="Draw Solar System")

## defining image buttons
planet1img = pygame.image.load('planet1.png') 
planet1btn = ImageButton(150,100,145,140,planet1img)

planet2img = pygame.image.load('planet2.png') 
planet2btn = ImageButton(325,100,131,128,planet2img)

planet3img = pygame.image.load('planet3.png') 
planet3btn = ImageButton(500,100,123,127,planet3img)

planet4img = pygame.image.load('planet4.png') 
planet4btn = ImageButton(150,275,125,128,planet4img)

planet5img = pygame.image.load('planet5.png') 
planet5btn = ImageButton(325,275,131,127,planet5img)

planet6img = pygame.image.load('planet6.png') 
planet6btn = ImageButton(500,275,115,115,planet6img)

planet7img = pygame.image.load('planet7.png') 
planet7btn = ImageButton(140,450,151,127,planet7img)

cometimg = pygame.image.load('comet.png') 
cometbtn = ImageButton(325,450,154,127,cometimg)

starimg = pygame.image.load('star.png') 
starbtn = ImageButton(530,450,90,127,starimg)




######## FUNCTIONS ###########
def newPlanetPage(screen):
    screen.fill((0,0,0)) ## clear screen
    
    running = True
    while running: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            ## checking if a button is pressed
            ## if pressed, it returns the function to draw the planet
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if planet1btn.isOver(pos):
                    return planet1
                elif planet2btn.isOver(pos):
                    return planet2
                elif planet3btn.isOver(pos):
                    return planet3
                elif planet4btn.isOver(pos):
                    return planet4
                elif planet5btn.isOver(pos):
                    return planet5
                elif planet6btn.isOver(pos):
                    return planet6
                elif planet7btn.isOver(pos):
                    return planet7
                elif cometbtn.isOver(pos):
                    return comet
                elif starbtn.isOver(pos):
                    return shootingStar

        ## writing instructions to select a planet icon
        instructionsFont = pygame.font.Font('FredokaOne-Regular.ttf',50)
        instructions = instructionsFont.render("Select an icon for your planet:",True,(255,255,255))
        screen.blit(instructions,(30,10))
        
        ## drawing buttons
        planet1btn.draw(screen)
        planet2btn.draw(screen)
        planet3btn.draw(screen)
        planet4btn.draw(screen)
        planet5btn.draw(screen)
        planet6btn.draw(screen)
        planet7btn.draw(screen)
        cometbtn.draw(screen)
        starbtn.draw(screen)

        ## updating screen
        pygame.display.update()


######## VARIABLES FOR TURTLE ####
functions = [sun]
days = []
distance = [0]


# game loop
running = True
        
while running:

    # screen background color
    screen.fill((0,0,0))

    # background image
    #screen.blit(background,(0,0))

    ## drawing buttons
    newPlanet.draw(screen)
    draw.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if newPlanet.isOver(pos):
                functions.append(newPlanetPage(screen))
                
    
    ## updating screen
    pygame.display.update()


