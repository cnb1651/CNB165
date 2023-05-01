import pygame
from game import Game
pygame.init()


#générer la fenêtre
pygame.display.set_caption("Street Fighter")
screen = pygame.display.set_mode((1850, 900))

background = pygame.image.load("C:/Users/User/Documents/projet_3/fond.png")

#charger le jeu
game = Game()

running = True

#boucle fenêtre
while running:
    
    #appliquer le bg
    screen.blit(background, (0,0))
    #appliquer les joueurs
    screen.blit(game.player1.image, game.player1.rect)
    # récupérer le gravier du joueur
    for gravier in game.player1.all_gravier:
        gravier.move()
    #appliquer le gravier sur le screen
    game.player1.all_gravier.draw(screen)
    
    #joueur gauche ou droite ?
    if game.pressed.get(pygame.K_d) and game.player1.rect.x < 1725:
        game.player1.move_right()
    elif game.pressed.get(pygame.K_q) and game.player1.rect.x > 0:
        game.player1.move_left()
    elif game.pressed.get(pygame.K_z):
        game.player1.move_up()
    elif game.pressed.get(pygame.K_s):
        game.player1.move_down()
        
    
    
    #le mettre à jour
    pygame.display.flip()
    
    #si on ferme
    for event in pygame.event.get():
        #fermeture ?
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture")
        
        # détecter les touches du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #détecter touche espace pr le projectile
            if event.key == pygame.K_SPACE:
                game.player1.launch_gravier()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False