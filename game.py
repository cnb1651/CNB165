import pygame
from player1 import Player1

#créer class représente jeu
class Game:
    def __init__(self):
        self.player1 = Player1()
        self.pressed = {}