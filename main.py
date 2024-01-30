import pygame, sys, asyncio
from pygame.locals import *

import menu
import player
import enemy
import defs

pygame.init()

p1 = player.Player() 
e1 = enemy.Enemy()
pygame.time.set_timer(defs.MORE_SPEED, 1000)

#Collision Checker
def checkIfCollision(p1,e1):
    if(p1.rect.colliderect(e1.rect)):
        return True
    

#Score Counter Font
font = pygame.font.Font('freesansbold.ttf', 32)


#Game loop begins
async def main():

    menu.main()

    while True:

        p1.update()
        e1.move()
        
        #Event Checker
        for event in pygame.event.get():
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


        text = font.render(str(defs.SCORE), True, "green", "white")
        textRect = text.get_rect()
        textRect.center = (20,20)
        
        HIGH_SCORE_text = font.render(str(defs.HIGH_SCORE), True, "green", "white")
        HIGH_SCORE_textRect = HIGH_SCORE_text.get_rect()
        HIGH_SCORE_textRect.center = (370, 20)

        defs.DISPLAYSURF.fill("white")

        if(checkIfCollision(p1,e1)):
            print("Game Over")
            if(defs.SCORE > defs.HIGH_SCORE):
                defs.HIGH_SCORE = defs.SCORE
            
            await asyncio.sleep(2)
            e1.__init__()
            p1.__init__()
            defs.SPEED=0
            defs.SCORE=0


        p1.draw(defs.DISPLAYSURF)
        e1.draw(defs.DISPLAYSURF)
        defs.DISPLAYSURF.blit(text, textRect)
        defs.DISPLAYSURF.blit(HIGH_SCORE_text, HIGH_SCORE_textRect)    

        pygame.display.update()
        defs.FRAMES_PER_SEC.tick(defs.FPS)
        await asyncio.sleep(0)

asyncio.run(main())