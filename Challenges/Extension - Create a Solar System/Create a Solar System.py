import pygame, sys
from pygame import mixer

 
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
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        
    def draw(self, screen):  # draws centralised buttons and text
        screen.blit(self.image, (self.x, self.y))

    def isOver(self, pos):  # detects if mouse positions is above buttons'
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
    

## defining buttons
font = pygame.font.SysFont('comicsans', 30, True)  
newPlanet = TextButton(300, 300, 210, 50, (172,146,237), text="New Planet")

testbuttonimg = pygame.image.load('buttonimg.jpg') 
imgbutton = ImageButton(100,100,testbuttonimg)




######## FUNCTIONS ###########
def newPlanetPage():
    running = True
    while running: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("F")

        ## writing instructions to select a planet icon
        instructionsFont = pygame.font.Font('FredokaOne-Regular.ttf',50)
        instructions = instructionsFont.render("Select an icon for your planet:",True,(255,255,255))
        screen.blit(instructions,(30,10))

        imgbutton.draw(screen)


        pygame.display.update()




# game loop
running = True
        
while running:

    # screen background color
    screen.fill((0,0,0))

    # background image
    #screen.blit(background,(0,0))

    ## drawing buttons
    newPlanet.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if newPlanet.isOver(pos):
                newPlanetPage()
                
    

    pygame.display.update()


