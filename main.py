import pygame, sys, random, asyncio, time
from pygame.locals import *


pygame.init()

#Game Variables
FPS = 60
MORE_SPEED = pygame.USEREVENT + 1
FRAMES_PER_SEC = pygame.time.Clock()
SPEED = 3
SCORE = 0

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('ball game')

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load("assets/anvil.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        self.rect.move_ip(0,SPEED)
        if(self.rect.bottom > SCREEN_HEIGHT):
            global SCORE
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("assets/balls.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,10)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     

p1 = Player() 
e1 = Enemy()
pygame.time.set_timer(MORE_SPEED, 1000)

#Collision Checker
def checkIfCollision(p1,e1):
    if(p1.rect.colliderect(e1.rect)):
        return True
    


#Score Counter Font
font = pygame.font.Font('freesansbold.ttf', 32)


#Game loop begins
async def main():
    global SPEED
    while True:

        #Event Checker
        for event in pygame.event.get():
            if event.type == MORE_SPEED:
                SPEED += 1
                print(SPEED)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        p1.update()
        e1.move()

        text = font.render(str(SCORE), True, "green", "white")
        textRect = text.get_rect()
        textRect.center = (20,20)

        DISPLAYSURF.fill("white")

        p1.draw(DISPLAYSURF)
        e1.draw(DISPLAYSURF)
        DISPLAYSURF.blit(text, textRect)
            

        if(checkIfCollision(p1,e1)):
            print("Game Over")
            time.sleep(2)
            pygame.quit()
            sys.exit()
        

        pygame.display.update()
        FRAMES_PER_SEC.tick(FPS)
        await asyncio.sleep(0)

asyncio.run(main())