import pygame
from settings import *


class Car(pygame.sprite.Sprite):

    def __init__(self, x, y, filename, up_key, down_key,right_key, left_key ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = P_SPEEDY
        self.up_key = up_key
        self.down_key = down_key
        self.right_key = right_key
        self.left_key = left_key
        self.left_score = 0
        self.right_score = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.up_key]:
            self.rect.x += self.speedy
        elif keys[self.down_key]:
           self.rect.x -= self.speedy

        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= SC_HEIGHT - P_HEIGHT:
            self.rect.y = SC_HEIGHT - P_HEIGHT


        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SC_WIDTH - WIDTH:
            self.rect.x = SC_WIDTH - WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_left_score(self):
        return self.left_score

    def get_right_score(self):
        return self.right_score
