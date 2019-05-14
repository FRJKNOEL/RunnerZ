'''Importation de pygame et des librairies locales'''
from pygame.locals import *
from random import randrange
import os,sys
sys.path.append ("../")
import pygame
import Pygame
import Pygame2
'''Importation de PygameMenu'''
import pygameMenu
from pygameMenu.locals import *

#------------------------------------------------------------------------------- variables ---------------------------------------------------------
'''textes du menu crédit'''
CREDIT = ['RUNNER Z - PROJET ISN 2018/2019'.format(pygameMenu.__version__),
         PYGAMEMENU_TEXT_NEWLINE,
         'Notre groupe: '.format(pygameMenu.__author__),
         PYGAMEMENU_TEXT_NEWLINE,
         'LEVENEUR Jean-Kenny, '.format(pygameMenu.__contributors__),
         'K/BIDI Maxime,'.format(pygameMenu.__contributors__),
         'HUET Kevin'.format(pygameMenu.__contributors__),]

'''textes du menu Controles'''
CONTROLS = ['Deplacement du personnage'.format(pygameMenu.__version__),
         PYGAMEMENU_TEXT_NEWLINE,
         '--> Avancer '.format(pygameMenu.__author__),
         PYGAMEMENU_TEXT_NEWLINE,
         '<-- Reculer, '.format(pygameMenu.__contributors__),
         PYGAMEMENU_TEXT_NEWLINE,
         '[Espace] Tirer,'.format(pygameMenu.__contributors__),
         PYGAMEMENU_TEXT_NEWLINE,
         '[P] Mettre le jeu en pause'.format(pygameMenu.__contributors__),]
COLOR_BACKGROUND = (40, 141, 177)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (40, 141, 177)
WINDOW_SIZE = (1280, 720)
#------------------------------------------------------------------------------- Pygame initialisation ---------------------------------------------
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

#---------------------------------------------------------------------- Création de la fenetre pygame et des objets --------------------------------
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Runner Z')
clock = pygame.time.Clock()
dt = 1 / FPS

NIVEAU = ['Ville']
#------------------------------------------------------------------------------- choix du niveau / parallax ----------------------------------------
def change_niveau(d):
    """
    Changer le niveau du jeu.
    """
    print ('Niveau choisi : {0}'.format(d))
    NIVEAU[0] = d


def play_function(niveau, font):
    niveau = niveau[0]
    assert isinstance(niveau, str)

    if niveau == 'Ville':
        Pygame.gameloop()
    elif niveau == 'Foret':
        Pygame2.gameloop()
    else:
        raise Exception('Niveau inconnu : {0}'.format(niveau))
#------------------------------------------------------------------------------- Arrière plan du menu ----------------------------------------------
def main_background():
    """
    Fonction menu - affiche l'arrière plan (couleur) quand il est actif
    """
    surface.fill(COLOR_BACKGROUND)
#---------------------------------------------------------------------------------------- Menu -----------------------------------------------------
'''choix du niveau'''
play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_XEN_GALAXIE,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1]),
                            menu_width=int(WINDOW_SIZE[0]),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Choix du niveau',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
# When pressing return -> play(NIVEAU[0], font)
play_menu.add_option('Jouer', play_function, NIVEAU,
                     pygame.font.Font(pygameMenu.fonts.FONT_XEN_GALAXIE, 30))
play_menu.add_selector('Selectionnez le niveau', [('Ville', 'Ville'),
                                             ('Foret', 'Foret')],

                       onreturn=None,
                       onchange=change_niveau)
play_menu.add_option('Retourner au menu', PYGAME_MENU_BACK)


'''Menu controles'''
controls_menu = pygameMenu.TextMenu(surface,
                               bgfun=main_background,
                               color_selected=COLOR_WHITE,
                               font=pygameMenu.fonts.FONT_XEN_GALAXIE,
                               font_color=COLOR_BLACK,
                               font_size_title=30,
                               font_title=pygameMenu.fonts.FONT_XEN_GALAXIE,
                               menu_color=MENU_BACKGROUND_COLOR,
                               menu_height=int(WINDOW_SIZE[1]),
                               menu_width=int(WINDOW_SIZE[0]),
                               onclose=PYGAME_MENU_DISABLE_CLOSE,
                               option_shadow=False,
                               text_color=COLOR_BLACK,
                               text_fontsize=30,
                               title='Controles',
                               window_height=WINDOW_SIZE[1],
                               window_width=WINDOW_SIZE[0]
                               )
for m in CONTROLS:
    controls_menu.add_line(m)
controls_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
controls_menu.add_option('Retourner au menu', PYGAME_MENU_BACK)

'''Menu crédit'''
credit_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_XEN_GALAXIE,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_XEN_GALAXIE,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_height=int(WINDOW_SIZE[1]),
                                 menu_width=int(WINDOW_SIZE[0]),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='Credits',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in CREDIT:
    credit_menu.add_line(m)
credit_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
credit_menu.add_option('Retourner au menu', PYGAME_MENU_BACK)

'''Menu'''
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_XEN_GALAXIE,
                            font_color=COLOR_BLACK,
                            font_size=40,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1]),
                            menu_width=int(WINDOW_SIZE[0]),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            joystick_enabled=True,
                            title='Runner Z',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Jouer', play_menu)
main_menu.add_option('Controles', controls_menu)
main_menu.add_option('Credits', credit_menu)
main_menu.add_option('Quitter', PYGAME_MENU_EXIT)

# ----------------------------------------------------------------------------- Boucle de lancement ------------------------------------------------
while True:

    '''Tick'''
    clock.tick(60)

    '''Application events'''
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    '''Menu'''
    main_menu.mainloop(events)

    '''Flip surface'''
    pygame.display.flip()
