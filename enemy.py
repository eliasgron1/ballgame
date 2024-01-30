import pygame
import random
import defs


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load("assets/anvil.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,defs.SCREEN_WIDTH-40),0)

    def move(self):
        self.rect.move_ip(0,defs.SPEED)
        if(self.rect.bottom > defs.SCREEN_HEIGHT):
            defs.SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 