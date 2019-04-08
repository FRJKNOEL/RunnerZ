import os, sys
import pygame
from pygame.locals import *
sys.path.append ("../")                                                                         #importation des différentes bibliothèques locales / fichier.py avec les différentes fonctions du jeu
import parallax                                                                                 #importation du parallax / arrière plan mobile
import nikita                                                                                   #importation du personnage

#-------------------------------------------------------------- création de la fenetre pygame --------------------------------------------------------------------
#white = (255,255,255)
#black = (0,0,0)
#red = (255,0,0)
#green = (0,155,0)
#BLUE = (40, 120, 230)
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.DOUBLEBUF)                                  #création de la fenetre pygame
pygame.display.set_caption('PlatformZ')                                                         #titre de la fenetre pygame
pygame.mouse.set_visible(1)                                                                     #afficher/cacher le curseur de souris (0:non visible / 1: visible)
clock = pygame.time.Clock()
player = nikita.Nikita((150, 490))                                                              #position sur la fenetre pygame du personnage
gameIcon = pygame.image.load('./assets/images/fond/icone.png')                                                       #création de l'icone de la fenetre pygame
pygame.display.set_icon(gameIcon)                                                               #affiche l'icone sur la fenetre pygame
#--------------------------------------------------------------------- Menu pause  -------------------------------------------------------------------------------
def pause():

    paused = True
    pause_musique = pygame.mixer.Sound("./assets/song/son.wav")

    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:                                                    #evenement clavier : appuie sur la touche "c" = arrête la boucle pause et retour au jeu
                if event.key == pygame.K_c:
                    pause_musique.stop()
                    pygame.mixer.unpause()
                    paused = False

                elif event.key == pygame.K_q:                                                   #evenement clavier : appuie sur la touche "a"(q --> clavier anglais) = ferme le jeu
                    pygame.quit()
                    quit()

        fond = pygame.image.load("./assets/images/fond/pause.png")
        screen.blit(fond, (0,0))
        pygame.display.update()
        clock.tick(5)

#--------------------------------------------------------------------------- Jeu  ---------------------------------------------------------------------------------
def gameloop():
    son = pygame.mixer.Sound("./assets/song/pause.wav")
    son.play()
    orientation = 'vertical'
    bg = parallax.ParallaxSurface((1280, 720), pygame.RLEACCEL)                                 #importations des différentes images du parallax ('...png')
                                                                                                #      + affectation d'une valeur pour la vitesse (', ...')
    bg.add('./assets/images/parallax/8.png', 8)
    bg.add('./assets/images/parallax/7.png', 7)
    bg.add('./assets/images/parallax/6.png', 6)
    bg.add('./assets/images/parallax/5.png', 5)
    bg.add('./assets/images/parallax/4.png', 4)
    bg.add('./assets/images/parallax/3.png', 3)
    bg.add('./assets/images/parallax/2.png', 2)
    bg.add('./assets/images/parallax/1.png', 1)
    run = True
    speed = 0
    t_ref = 0
    while run:                                                                                  #définition des différentes interractions
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                paused = False
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                speed += 10
            if event.type == KEYDOWN and event.key == K_LEFT:
                speed -= 10
            if event.type == KEYDOWN and event.key == K_DOWN:
                orientation = 'horizontal'
            if event.type == KEYDOWN:
                if event.key == pygame.K_p :
                    pygame.mixer.pause()
                    pause_musique = pygame.mixer.Sound("./assets/song/son.wav")
                    pause_musique.play()
                    paused = True
                    pause()
        bg.scroll(speed, orientation)                                                           #mouvement du parallax
        t = pygame.time.get_ticks()
        if (t - t_ref) > 60:
            bg.draw(screen)
            pygame.display.flip()
        player.handle_event(event)                                                              #evenement du personnage
        screen.blit(player.image, player.rect)                                                  #affiche le personnage sur la fenetre pygame
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()
