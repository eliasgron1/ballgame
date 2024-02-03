import pygame
import defs
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.set_skin()
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)



    def set_skin(self):
        if(defs.CURRENT_SKIN=="goku"):
             self.image = pygame.image.load("assets/goku.png")
        elif(defs.CURRENT_SKIN=="jager"):
             self.image = pygame.image.load("assets/jager.png")
        elif(defs.CURRENT_SKIN=="anvil"):
             self.image = pygame.image.load("assets/anvil.png")
        else:
            self.image = pygame.image.load("assets/balls.png")


    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
        if self.rect.bottom < defs.SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,10)
                     
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < defs.SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

    def finger_move(self,x,y):
        self.rect.center = (x, y)

        
    def draw(self, surface):
        surface.blit(self.image, self.rect)     