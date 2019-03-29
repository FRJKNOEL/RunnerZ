# Importation de pygame et des librairies locales
from pygame.locals import *
from random import randrange
import os
import pygame
import Pygame
#Importation de PygameMenu
import pygameMenu
from pygameMenu.locals import *

ABOUT = ['RUNNER Z - PROJET ISN 2018/2019'.format(pygameMenu.__version__),
         'Notre groupe: LEVENEUR Jean-Kenny, K/BIDI Maxime, HUET Kevin'.format(pygameMenu.__author__),
         PYGAMEMENU_TEXT_NEWLINE,]
COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
WINDOW_SIZE = (1280, 720)
# -----------------------------------------------------------------------------
# Pygame initialisation
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Création de la fenetre pygame et des objets
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Runner Z')
clock = pygame.time.Clock()
dt = 1 / FPS
# -----------------------------------------------------------------------------
def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    surface.fill(COLOR_BACKGROUND)
# -----------------------------------------------------------------------------
# Menu crédit
about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1] * 1),
                                 menu_width=int(WINDOW_SIZE[0] * 1),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='Credit',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Retourner au menu', PYGAME_MENU_BACK)

# Menu
main_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1] * 1),
                            menu_width=int(WINDOW_SIZE[0] * 1),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Runner Z',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )
main_menu.add_option('Jouer', Pygame.gameloop)
main_menu.add_option('Credit', about_menu)
main_menu.add_option('Quitter', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
# Boucle de lancement
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()
