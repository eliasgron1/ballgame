import pygame, sys, asyncio
from pygame.locals import *

import defs
import button
import menu


pygame.init()

p1 = defs.PLAYER
e1 = defs.ENEMY 

pygame.time.set_timer(defs.MORE_SPEED, 1000)

#Collision Checker
def checkIfCollision(p1,e1):
    if(p1.rect.colliderect(e1.rect)):
        return True
    

#Score Counter Font
font = pygame.font.Font('freesansbold.ttf', 32)

#Settings Button
gear_img = pygame.image.load('assets/gear.png').convert_alpha()
settings_button = button.Button(380 ,580, gear_img, 1)



#Main loop begins
async def main():
    print("starting main")

    while True:

        #Run Menu
        if(defs.GAME_PAUSED):
            menu.menu()


        
        #Run Game
        else:
            p1.update()
            e1.move()
            
            
            #Event Checker
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                     defs.GAME_PAUSED=True
                if event.type == defs.MORE_SPEED:
                    defs.SPEED += 1
                    print(defs.SPEED)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # For Mobile Devices
                if event.type == pygame.FINGERDOWN:
                    print("debug:event.type=FINGERDOWN")
                    x = event.x * defs.SCREEN_WIDTH
                    y = event.y * defs.SCREEN_HEIGHT
                    p1.finger_move(x,y)

                if event.type == pygame.FINGERUP:
                    print("debug:event.type=FINGERUP")
                    #fingers.pop(event.finger_id, None)


            SCORE = font.render(str(defs.SCORE), True, "green", "white")
            SCORE_rect = SCORE.get_rect()
            SCORE_rect.center = (20,20)
            
            HIGH_SCORE_text = font.render(str(defs.HIGH_SCORE), True, "green", "white")
            HIGH_SCORE_textRect = HIGH_SCORE_text.get_rect()
            HIGH_SCORE_textRect.center = (370, 20)

            defs.DISPLAYSURF.fill("white")

            #Chech for collisision
            if(checkIfCollision(p1,e1)):
                print("Game Over")
                if(defs.SCORE > defs.HIGH_SCORE):
                    defs.HIGH_SCORE = defs.SCORE
                
                #Restart Game
                await asyncio.sleep(2)
                e1.__init__()
                p1.__init__()
                defs.SPEED=0
                defs.SCORE=0

            
            #Draw Content To Screen
            if settings_button.draw(defs.DISPLAYSURF):
                defs.GAME_PAUSED = True

            p1.draw(defs.DISPLAYSURF)
            e1.draw(defs.DISPLAYSURF)
            defs.DISPLAYSURF.blit(SCORE, SCORE_rect)
            defs.DISPLAYSURF.blit(HIGH_SCORE_text, HIGH_SCORE_textRect)    

            pygame.display.update()
            defs.FRAMES_PER_SEC.tick(defs.FPS)
            
        await asyncio.sleep(0)


asyncio.run(main())