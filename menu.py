import pygame
import button
import defs

#create game window
SCREEN_WIDTH = defs.SCREEN_WIDTH
SCREEN_HEIGHT = defs.SCREEN_HEIGHT

#game variables
menu_state = "main"

def menu():
    global menu_state

    #Load button images
    resume_img = pygame.image.load("assets/play_button.png").convert_alpha()
    skins_img = pygame.image.load("assets/skins_button.png").convert_alpha()
    back_img = pygame.image.load('assets/back_button.png').convert_alpha()

    #Create button instances
    resume_button = button.Button(50, 525, resume_img, 1)
    skins_button = button.Button(200, 525, skins_img, 1)
    back_button = button.Button(125, 10, back_img, 1)

    #Skin Selection
    default_skin = pygame.image.load("assets/balls.png").convert_alpha()
    goku_skin = pygame.image.load("assets/goku.png").convert_alpha()

    #Skin instances for menu
    default_skin_button = button.Button(100, 100, default_skin, 1)
    goku_skin_button = button.Button(150, 100, goku_skin, 1)


    defs.DISPLAYSURF.fill((52, 78, 91))

    #check menu state
    if menu_state == "main":
    #draw pause screen buttons
        if resume_button.draw(defs.DISPLAYSURF):
            defs.GAME_PAUSED = False
        if skins_button.draw(defs.DISPLAYSURF):
                menu_state = "skins"


    #check if the skins menu is open
    if menu_state == "skins":
        #Draw and check if back button pressed 
        if back_button.draw(defs.DISPLAYSURF):
                menu_state = "main"
        #Draw and check if skin button pressed
        if default_skin_button.draw(defs.DISPLAYSURF):
            defs.CURRENT_SKIN = "default"
            defs.GAME_PAUSED=False
        if goku_skin_button.draw(defs.DISPLAYSURF):
            defs.CURRENT_SKIN = "goku"
            defs.GAME_PAUSED=False
        defs.PLAYER.set_skin()

    #Event Checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            defs.GAME_PAUSED = False

    pygame.display.update()
