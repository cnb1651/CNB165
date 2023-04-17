import pygame
pygame.init()


#créer class représente jeu
class Game:
    def __init__(self):
        self.player1 = Player1()


#créer une classe pr le joueur
class Player1(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

#générer la fenêtre
pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((1000, 600))

background = pygame.image.load("Desktop/1.png")

#chrager le jeu
game = Game()

running = True

#boucle fenêtre
while running:
    
    #appliquer le bg
    screen.blit(background, (0,0))
    #appliquer les joueurs
    screen.blit(game.player1.image, game.player1.rect)
    #le mettre à jour
    pygame.display.flip()
    
    #si on ferme
    for event in pygame.event.get():
        #fermeture ?
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture")