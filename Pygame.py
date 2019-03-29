import os, sys
import pygame
from pygame.locals import *
sys.path.append ("../")                                                                         #importation des différentes bibliothèques locales / fichier.py avec les différentes fonctions du jeu
import parallax                                                                                 #importation du parallax / arrière plan mobile
import nikita                                                                                   #importation du personnage

#-------------------------------------------------------------- création de la fenetre pygame --------------------------------------------------------------------
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
BLUE = (40, 120, 230)
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.DOUBLEBUF)                                  #création de la fenetre pygame
pygame.display.set_caption('PlatformZ')                                                         #titre de la fenetre pygame
pygame.mouse.set_visible(0)                                                                     #afficher/cacher le curseur de souris (0:non visible / 1: visible)
clock = pygame.time.Clock() 
player = nikita.Nikita((150, 490))                                                              #position sur la fenetre pygame du personnage 
gameIcon = pygame.image.load('./assets/images/fond/icone.png')                                                       #création de l'icone de la fenetre pygame
pygame.display.set_icon(gameIcon)                                                               #affiche l'icone sur la fenetre pygame
smallfont = pygame.font.SysFont("Comic Sans MS,Arial", 25)
medfont = pygame.font.SysFont("Comic Sans MS,Arial", 50)
largefont = pygame.font.SysFont("Comic Sans MS,Arial", 80)

#-------------------------------------------------------------- création du menu pause  --------------------------------------------------------------------------
def text_objects(text,color,size):                                                              #taille de la police d'écriture
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size = "small"):                                 #texte du menu pause
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (1280 / 2), (720 / 2)+y_displace
    screen.blit(textSurf, textRect)
#--------------------------------------------------------------------- Menu pause  -------------------------------------------------------------------------------
def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:                                                    #evenement clavier : appuie sur la touche "c" = arrête la boucle pause et retour au jeu
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:                                                   #evenement clavier : appuie sur la touche "a"(q --> clavier anglais) = ferme le jeu
                    pygame.quit()
                    quit()
        fond = pygame.image.load("./assets/images/fond/pause.png")
        screen.blit(fond, (0,0))
        message_to_screen("Pause",
                          white,
                          -100,
                          size="large")

        message_to_screen("Appuyez sur C pour continuer ou A pour quitter.",
                          white,
                          25)
        message_to_screen("Choisir le personnage : -1 /Nikita, -2 /Rita.",
                          white,
                          55)
        pygame.display.update()
        clock.tick(5)
#------------------------------------------------------------------------- Musique ------------------------------------------------------------------------------------------
def musique():

    musique_statut = True

    while musique_statut:
        son = pygame.mixer.Sound("./assets/song/pause.wav")
        son.play()
    
#------------------------------------------------------------------------- Menu choix du personnage / parallax --------------------------------------------------------------
def choix_niveau():

    choix = True

    while choix:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:                                                    #evenement clavier : appuie sur la touche "c" = arrête la boucle pause et retour au jeu
                if event.key == pygame.K_c:
                    choix = False
                if event.key == pygame.K_1:                                                     #evenement clavier: appuie sur la touche "1" = lance la fonction niveau_1 (gère le parallax 1)
                    choix = False
                    niveau_1()
                elif event.key == pygame.K_q:                                                   #evenement clavier : appuie sur la touche "a"(q --> clavier anglais) = ferme le jeu
                    pygame.quit()
                    quit()
        fond2 = pygame.image.load("./assets/images/choix_niveau.jpg")
        screen.blit(fond2, (0,0))
        message_to_screen("Choix du parallax",
                          black,
                          -100,
                          size="large")

        message_to_screen("Appuyez sur 1 pour la ville ou 2 pour la fôret.",
                          black,
                          25)
        pygame.display.update()
        clock.tick(5)

def niveau_1():
    orientation = 'vertical'
    bg = parallax.ParallaxSurface((1280, 720), pygame.RLEACCEL)                                 #importations des différentes images du parallax ('...png') 
                                                                                                #      + affectation d'une valeur pour la vitesse (', ...')
    bg.add('8.png', 8)
    bg.add('7.png', 7)
    bg.add('6.png', 6)
    bg.add('5.png', 5)
    bg.add('4.png', 4)
    bg.add('3.png', 3)
    bg.add('2.png', 2)
    bg.add('1.png', 1)
    return(niveau_1)

def niveau_2():
    orientation = 'vertical'
    bg = parallax.ParallaxSurface((1280, 720), pygame.RLEACCEL)                                 #importations des différentes images du parallax ('...png') 
                                                                                                #      + affectation d'une valeur pour la vitesse (', ...')
    bg.add('1.7.png', 7)
    bg.add('1.6.png', 6)
    bg.add('1.5.png', 5)
    bg.add('1.4.png', 4)
    bg.add('1.3.png', 3)
    bg.add('1.2.png', 2)
    bg.add('1.1.png', 1)
    return(niveau_2)

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
                music_statut = False
                run = False
                paused = False
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                speed += 10
            if event.type == KEYUP and event.key == K_RIGHT:
                speed -= 10
            if event.type == KEYDOWN and event.key == K_LEFT:
                speed -= 10
            if event.type == KEYUP and event.key == K_LEFT:
                speed += 10
            if event.type == KEYDOWN and event.key == K_DOWN:
                orientation = 'horizontal'
            if event.type == KEYDOWN:
                if event.key == pygame.K_p :
                    paused = True
                    pause()
                if event.key == pygame.K_o :
                    choix = True
                    choix_niveau()
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