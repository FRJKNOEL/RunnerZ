import os, sys
import pygame
from pygame.locals import *
sys.path.append ("../")                                                                         #importation des différentes bibliothèques locales / fichier.py avec les différentes fonctions du jeu
import parallax                                                                                 #importation du parallax / arrière plan mobile
import nikita                                                                                   #importation du personnage
import zombie
import balle
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
balles = []
wave_zombie = 5
wave = 1
nbzombie_wave = 5
for i in range(wave_zombie):
    zombies.append(zombie.Zombie((1000 + i * 100,490)))
gameIcon = pygame.image.load('./assets/images/fond/logo1.png')                                   #création de l'icone de la fenetre pygame
pygame.display.set_icon(gameIcon)                                                                #affiche l'icone sur la fenetre pygame

#--------------------------------------------------------------------- Menu pause  ------------------------------------------------------------------------------
def main_background():
    """
    Fonction menu - affiche l'arrière plan (couleur) quand il est actif
    """
    screen.fill(COLOR_BACKGROUND)
    
def pause():

    paused = True

    while paused:
        PAUSE = ['PAUSE'.format(pygameMenu.__version__),]
        pause_menu = pygameMenu.Menu(screen,
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
                                    title='PAUSE',
                                    window_height=WINDOW_SIZE[1],
                                    window_width=WINDOW_SIZE[0]
                                    )
        pause_menu.add_option('Reprendre', gameloop)
        pause_menu.add_option('Quitter', PYGAME_MENU_EXIT)
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                paused = False
                exit()
        pause_menu.mainloop(events)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(5)
#--------------------------------------------------------------------------- Gameover -----------------------------------------------------------------------------------
def gameover():
    gameover = True
    while gameover:
        gameover_menu = pygameMenu.Menu(screen,
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
                                    title='GAMEOVER',
                                    window_height=WINDOW_SIZE[1],
                                    window_width=WINDOW_SIZE[0]
                                    )
        gameover_menu.add_option('Quitter', PYGAME_MENU_EXIT)
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                paused = False
                exit()
        gameover_menu.mainloop(events)
        pygame.display.flip()
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
#--------------------------------------------------------------------- Affichage nombre vagues /zombies  -----------------------------------------------------------
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('./pygameMenu/fonts/xen_galaxy.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((180),(20))
    screen.blit(TextSurf, TextRect)
#--------------------------------------------------------------------------- vagues de zombies / collisions --------------------------------------------------------
def waves_system(player, z):
    global wave
    global wave_zombie
    if z.life <= 0:
        pass
    elif player.rect.colliderect(z.rect):
        player.life -= 1
        z.life = 0

def checkCollision(b,z):
    global wave
    global wave_zombie
    if (z.life > 0 for z in zombies):
        if b.life <= 0:
            pass
        elif b.rect.colliderect(z.rect):
            b.life = 0
            z.life = 0
            balles.remove(b)

def spawn(z):
    global wave
    global wave_zombie
    if all(z.life <= 0 for z in zombies):
        wave_zombie = wave_zombie + 1
        wave = wave + 1
        zombies.clear()
        pygame.time.set_timer(pygame.USEREVENT, 3000)
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
    global wave_zombie
    global wave
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

            if event.type == KEYDOWN and event.key == K_SPACE:
                balles.append(balle.Balle(((player.rect.x),(player.rect.y + 50)), 'right'))
                shoot = pygame.mixer.Sound("./assets/song/shoot.wav")
                shoot.play()

            if event.type == pygame.USEREVENT:
                for i in range(wave_zombie):
                    zombies.append(zombie.Zombie((1000 + i * 100,490)))
                    pygame.time.set_timer(pygame.USEREVENT, 0)

            if event.type == KEYDOWN and event.key == K_p :
                pygame.mixer.pause()
                paused = True
                pause()
                
        bg.scroll(speed, orientation)                                                           #mouvement du parallax
        t = pygame.time.get_ticks()
        if (t - t_ref) > 60:
            bg.draw(screen)
        systeme_vie()
                                                         
        for z in zombies:
            if z.life > 0:
                z.handle_event(event)
                screen.blit(z.image,z.rect)
                waves_system(player, z)
            for b in balles:
                if b.life > 0:
                    b.handle_event(event)
                    screen.blit(b.image, b.rect)
                    checkCollision(b ,z)
                    spawn(z)

        player.handle_event(event)                                                              #evenement du personnage  
        screen.blit(player.image, player.rect)                                                  #affiche le personnage sur la fenetre pygame
        nbzombie_wave = sum(z.life for z in zombies)
        message_display('Vague : ' +str(wave) + ' Nombre de Zombies : '+str(nbzombie_wave))
        pygame.display.flip()
        clock.tick(10)
        if player.life == 0 :
            gameover()
    pygame.quit()
