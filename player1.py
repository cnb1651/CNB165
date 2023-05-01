import pygame
from gravier import Gravier

#créer une classe pr le joueur
class Player1(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 10
        self.all_gravier = pygame.sprite.Group()
        self.image = pygame.image.load('C:/Users/User/Documents/projet_3/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 700
    
    def launch_gravier(self):
        self.all_gravier.add(Gravier(self))
    
    def move_right(self):
        self.rect.x += self.velocity
        
    def move_left(self):
        self.rect.x -= self.velocity
        
    def move_up(self):
        self.rect.y -= self.velocity        
        
    def move_down(self):
        self.rect.y += self.velocity