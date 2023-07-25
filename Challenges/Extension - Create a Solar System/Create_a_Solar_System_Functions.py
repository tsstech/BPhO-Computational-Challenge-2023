import pygame, sys
from Drawing_Planets_Functions import *

# Initialize program
pygame.init()


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
font = pygame.font.Font("FredokaOne-Regular.ttf", 30)  

submit = TextButton(50, 470, 150, 50, ("#84A7BA"), text="Submit")
home = TextButton(330, 520, 150, 50, ("#84A7BA"), text="Home")


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



############## FUNCTIONS ##############

## Function for 1st page to create a new planet
## This page lets user select an icon for the planet
def newPlanetPage(screen):
    screen.fill("#303655") ## clear screen
    
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
                    return planet1, "planet1"
                elif planet2btn.isOver(pos):
                    return planet2, "planet"
                elif planet3btn.isOver(pos):
                    return planet3, "planet3"
                elif planet4btn.isOver(pos):
                    return planet4, "planet4"
                elif planet5btn.isOver(pos):
                    return planet5, "planet5"
                elif planet6btn.isOver(pos):
                    return planet6, "planet6"
                elif planet7btn.isOver(pos):
                    return planet7, "planet7"
                elif cometbtn.isOver(pos):
                    return comet, "comet"
                elif starbtn.isOver(pos):
                    return shootingStar, "shootingStar"

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







## Function for 2nd page to create a new planet
## This page lets user input orbit length & distance from sun for the planet
def daysPage(screen):
    screen.fill("#303655") ## clear screen

    ## writing instructions to input orbit length
    instructionsFont = pygame.font.Font('FredokaOne-Regular.ttf',50)
    instructions = instructionsFont.render("How long is the orbit in days?",True,(255,255,255))
    screen.blit(instructions,(50,50))

    ## writing instructions to input distance from sun
    instructionsFont = pygame.font.Font('FredokaOne-Regular.ttf',50)
    instructions = instructionsFont.render("How far is the planet?",True,(255,255,255))
    screen.blit(instructions,(50,270))

    ## input text box
    daysInputRect = pygame.Rect(50, 140, 190, 52)
    distanceInputRect = pygame.Rect(50, 360, 190, 52)

    ## input text & font
    baseFont = pygame.font.Font('FredokaOne-Regular.ttf',40)
    daysInput = ""
    distanceInput = ""

    ## variables that check if user is typing in textbox
    daysTyping = False
    distanceTyping = False

    
    running = True
    while running: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if daysInputRect.collidepoint(pos): # if user clicks on textfield for orbit length
                    daysTyping = True                    # set typing to true
                else:
                    daysTyping = False

                if distanceInputRect.collidepoint(pos): # if user clicks on textfield for orbit length
                    distanceTyping = True                    # set typing to true
                else:
                    distanceTyping = False

                if submit.isOver(pos):      # if user clicks submit button
                    return int(daysInput), int(distanceInput+"000000")   # return days

            if daysTyping == True:      # if user is typing in days textfield
                if event.type == pygame.KEYDOWN:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
          
                        # get text input from 0 to -1 i.e. end.
                        daysInput = daysInput[:-1]
          
                    # Unicode standard is used for string
                    # formation
                    else:
                        daysInput += event.unicode

            elif distanceTyping == True:      # if user is typing in days textfield
                if event.type == pygame.KEYDOWN:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
          
                        # get text input from 0 to -1 i.e. end.
                        distanceInput = distanceInput[:-1]
          
                    # Unicode standard is used for string
                    # formation
                    else:
                        distanceInput += event.unicode
            
            
        ## draw input box
        #pygame.draw.rect(screen, "#BFCBCE", daysInputRect)  CHOOSE COLOUR #####
        pygame.draw.rect(screen, "#6F90AF", daysInputRect)
  
        ## writing user text as they type
        textSurface = baseFont.render(daysInput, True, (255, 255, 255))
        screen.blit(textSurface, (daysInputRect.x+10, daysInputRect.y+3))
        daysInputRect.w = max(100, textSurface.get_width()+10)  ## set textfield width

        textSurface = baseFont.render("days", True, (255, 255, 255))
        screen.blit(textSurface, (daysInputRect.x+200, daysInputRect.y+3))

        ## draw input box
        #pygame.draw.rect(screen, "#BFCBCE", daysInputRect)  CHOOSE COLOUR #####
        pygame.draw.rect(screen, "#6F90AF", distanceInputRect)
  
        ## writing user text as they type
        textSurface = baseFont.render(distanceInput, True, (255, 255, 255))
        screen.blit(textSurface, (distanceInputRect.x+10, distanceInputRect.y+3))
        distanceInputRect.w = max(100, textSurface.get_width()+10)  ## set textfield width

        textSurface = baseFont.render("million miles", True, (255, 255, 255))
        screen.blit(textSurface, (distanceInputRect.x+200, distanceInputRect.y+3))
        
        ## draw submit button
        submit.draw(screen)
                    
        ## updating screen
        pygame.display.update()






## Function for page to display all created planets
def showPlanetsPage(screen,days,functions,distances):
    screen.fill("#303655") ## clear screen

    ## writing page title
    titleFont = pygame.font.Font('FredokaOne-Regular.ttf',50)
    title = titleFont.render("My Planets",True,(255,255,255))
    screen.blit(title,(260,20))
    

    ## loop variables
    imgs = {"planet1" : planet1img,
            "planet2" : planet2img,
            "planet3" : planet3img,
            "planet4" : planet4img,
            "planet5" : planet5img,
            "planet6" : planet6img,
            "planet7" : planet7img,
            "comet" : cometimg,
            "shootingStar" : starimg}
    
    running = True
    while running:

        ## draw back to home button
        home.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if home.isOver(pos):    ## if home button is clicked 
                    return None

        textFont = pygame.font.Font('Fredoka-Regular.ttf',20)
        ## run through planets and draw onto screen
        for i in range(len(functions)):
            if i < 3:   ## if it is up to the 3rd planet, write on 1st column
                ## planet icon
                screen.blit(imgs[functions[i]], (85, 90+(150*(i))))
                ## days
                day = textFont.render(f"Days: {days[i-1]}",True,(255,255,255))
                screen.blit(day,(250,100+(150*(i))))
                ## distance
                distance1 = textFont.render("Distance:",True,(255,255,255))
                screen.blit(distance1,(250,140+(150*(i))))
                distance2 = textFont.render(f"{distances[i+1]}",True,(255,255,255))
                screen.blit(distance2,(250,175+(150*(i))))
            else:   ## if it is after the 3rd planet, write on 2nd column
                ## planet icon
                screen.blit(imgs[functions[i]], (450, 90+(150*(i-3))))
                ## days
                day = textFont.render(f"Days: {days[i-1]}",True,(255,255,255))
                screen.blit(day,(600,100+(150*(i-3))))
                ## distance
                distance1 = textFont.render("Distance:",True,(255,255,255))
                screen.blit(distance1,(600,140+(150*(i-3))))
                distance2 = textFont.render(f"{distances[i+1]}",True,(255,255,255))
                screen.blit(distance2,(600,175+(150*(i-3))))
        
        
        ## updating screen
        pygame.display.update()

