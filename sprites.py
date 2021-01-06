import pygame
import os
from os import path
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.player_img = pygame.image.load(path.join(self.img_dir, "player_00.png")).convert()
        self.image = self.player_img
        #self.image = pygame.Surface((30, 30))
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 96
        self.speedx = 0
        self.speedy = 0        

    def update(self):
        pass
        
