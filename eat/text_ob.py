import pygame
from settings import *

class Text_Ob:

    def __init__(self, x, y, health, screen):
        self.x = x
        self.y = y
        self.health = health
        self.screen = screen
        self.font = pygame.font.SysFont('arial', 32)
        

    def update(self, health):
        self.health = health
        self.text = self.font.render(str(self.health), True, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect = (self.x, self.y)

    def draw(self):
        self.screen.blit(self.text, self.text_rect)
