import pygame
import button
import defs

#create game window
SCREEN_WIDTH = defs.SCREEN_WIDTH
SCREEN_HEIGHT = defs.SCREEN_HEIGHT

#game variables

def menu():

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
    jager_skin = pygame.image.load("assets/jager.png").convert_alpha()
    anvil_skin = pygame.image.load("assets/anvil.png").convert_alpha()

    #Skin instances for menu
    default_skin_button = button.Button(50, 100, default_skin, 1)
    goku_skin_button = button.Button(125, 100, goku_skin, 1)
    jager_skin_button = button.Button(200, 100, jager_skin, 1)
    anvil_skin_button = button.Button(275, 100, anvil_skin, 1)

    defs.DISPLAYSURF.fill((52, 78, 91))

    #check menu state
    if defs.MENU_STATE == "main":
    #draw pause screen buttons
        if resume_button.draw(defs.DISPLAYSURF):
            defs.GAME_PAUSED = False
        if skins_button.draw(defs.DISPLAYSURF):
                defs.MENU_STATE = "skins"


    #check if the skins menu is open
    if defs.MENU_STATE == "skins":
        #Draw and check if back button pressed 
        if back_button.draw(defs.DISPLAYSURF):
                defs.MENU_STATE = "main"
        #Draw and check if skin button pressed
        if default_skin_button.draw(defs.DISPLAYSURF):
            defs.CURRENT_SKIN = "default"
            defs.GAME_PAUSED=False
        if goku_skin_button.draw(defs.DISPLAYSURF):
            defs.CURRENT_SKIN = "goku"
            defs.GAME_PAUSED=False
        if jager_skin_button.draw(defs.DISPLAYSURF):
            defs.CURRENT_SKIN = "jager"
            defs.GAME_PAUSED=False
        if anvil_skin_button.draw(defs.DISPLAYSURF):
            defs.CURRENT_SKIN = "anvil"
            defs.GAME_PAUSED=False
        defs.ENEMY.__init__()
        defs.PLAYER.__init__()
        defs.SPEED=0
        defs.SCORE=0

    #Event Checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            defs.GAME_PAUSED = False

    pygame.display.update()
