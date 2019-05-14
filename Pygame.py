import os, sys
import pygame
from pygame.locals import *
sys.path.append ("../")                                                                         #importation des différentes bibliothèques locales / fichier.py avec les différentes fonctions du jeu
import parallax                                                                                 #importation du parallax / arrière plan mobile
import nikita                                                                                   #importation du personnage
import zombie
import pygameMenu
from pygameMenu.locals import *
#-------------------------------------------------------------- création de la fenetre pygame --------------------------------------------------------------------
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
BLUE = (40, 120, 230)
COLOR_BACKGROUND = (40, 141, 177)
MENU_BACKGROUND_COLOR = (40, 141, 177)
WINDOW_SIZE = (1280, 720)
pygame.init()
screen = pygame.display.set_mode((1280, 720),pygame.DOUBLEBUF)                                  #création de la fenetre pygame
pygame.display.set_caption('Runner Z')                                                          #titre de la fenetre pygame
pygame.mouse.set_visible(0)                                                                     #afficher/cacher le curseur de souris (0:non visible / 1: visible)
clock = pygame.time.Clock() 
player = nikita.Nikita((150, 490))                                                              #position sur la fenetre pygame du personnage 
zombies = []
gameIcon = pygame.image.load('./assets/images/fond/logo.png')                                   #création de l'icone de la fenetre pygame
pygame.display.set_icon(gameIcon)                                                               #affiche l'icone sur la fenetre pygame
#--------------------------------------------------------------------- Menu pause  ------------------------------------------------------------------------------
def main_background():
    """
    Fonction menu - affiche l'arrière plan (couleur) quand il est actif
    """
    screen.fill(COLOR_BACKGROUND)
    
def pause():

    paused = True

    while paused:
        main_menu = pygameMenu.Menu(screen,
                                    bgfun=main_background,
                                    color_selected=white,
                                    font=pygameMenu.fonts.FONT_XEN_GALAXIE,
                                    font_color=black,
                                    font_size=40,
                                    menu_alpha=100,
                                    menu_color=MENU_BACKGROUND_COLOR,
                                    menu_height=int(WINDOW_SIZE[1]),
                                    menu_width=int(WINDOW_SIZE[0]),
                                    onclose=PYGAME_MENU_DISABLE_CLOSE,
                                    option_shadow=False,
                                    title='Runner Z',
                                    window_height=WINDOW_SIZE[1],
                                    window_width=WINDOW_SIZE[0]
                                    )
        main_menu.add_option('Reprendre', gameloop)
        main_menu.add_option('Quitter', PYGAME_MENU_EXIT)
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                paused = False
                exit()
        main_menu.mainloop(events)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(5)
#--------------------------------------------------------------------------- Gameover -----------------------------------------------------------------------------------
def gameover():
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:                                                    #evenement clavier : appuie sur la touche "c" = arrête la boucle pause et retour au jeu
                if event.key == pygame.K_q:                                                   #evenement clavier : appuie sur la touche "a"(q --> clavier anglais) = ferme le jeu
                    pygame.quit()
                    quit()
        fond = pygame.image.load("./assets/images/fond/ko.png")
        screen.blit(fond, (0,0))
        pygame.display.update()
        clock.tick(5)
#--------------------------------------------------------------------------- Vie -----------------------------------------------------------------------------------
def systeme_vie():
    if player.life == 6 :
        testvie = pygame.image.load("./assets/images/vie/6.png")
        screen.blit(testvie, (0,0))
        pygame.display.flip()
    if player.life == 5:
        testvie = pygame.image.load("./assets/images/vie/5.png")
        screen.blit(testvie, (0,0))
        pygame.display.flip()
    if player.life == 4:
        testvie = pygame.image.load("./assets/images/vie/4.png")
        screen.blit(testvie, (0,0))
        pygame.display.flip()
    if player.life == 3:
        testvie = pygame.image.load("./assets/images/vie/3.png")
        screen.blit(testvie, (0,0))
        pygame.display.flip()
    if player.life == 2:
        testvie = pygame.image.load("./assets/images/vie/2.png")
        screen.blit(testvie, (0,0))
        pygame.display.flip()
    if player.life == 1:
        testvie = pygame.image.load("./assets/images/vie/1.png")
        screen.blit(testvie, (0,0))
        pygame.display.flip()
#--------------------------------------------------------------------------- collisions ----------------------------------------------------------------------------
def checkCollision(player, z):
    if z.life <= 0:
        pass
    elif player.rect.colliderect(z.rect):
        player.life -= 1
        z.life = 0
#--------------------------------------------------------------------------- Jeu  ---------------------------------------------------------------------------------
def gameloop():
    son = pygame.mixer.Sound("./assets/song/runnerz.wav")
    son.play()
    orientation = 'horizontal'
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
    wave = 5
    for i in range(wave):
        zombies.append(zombie.Zombie((1000 + i * 100,490)))
    while run:                                                                                  #définition des différentes interractions (parallax)
        for event in pygame.event.get():
            if event.type == QUIT:
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
                    pygame.mixer.pause()
                    paused = True
                    pause()
        bg.scroll(speed, orientation)                                                           #mouvement du parallax
        t = pygame.time.get_ticks()
        if (t - t_ref) > 60:
            bg.draw(screen)
        systeme_vie()
        player.handle_event(event)                                                              #evenement du personnage  
        screen.blit(player.image, player.rect)                                                  #affiche le personnage sur la fenetre pygame
        for z in zombies:
            if z.life > 0:
                z.handle_event(event)
                screen.blit(z.image,z.rect)
                checkCollision(player, z)        
        pygame.display.flip()
        clock.tick(10)
        if player.life == 0 :
            gameover()
    pygame.quit()
