# coding=utf-8
# Get actual folder
import os

__actualpath = str(os.path.abspath(
    os.path.dirname(__file__))).replace('\\', '/')
__fontdir = '{0}/fonts/{1}.ttf'

# Avaiable fonts
FONT_8BIT = __fontdir.format(__actualpath, '8bit')
FONT_BEBAS = __fontdir.format(__actualpath, 'bebas')
FONT_FRANCHISE = __fontdir.format(__actualpath, 'franchise')
FONT_MUNRO = __fontdir.format(__actualpath, 'munro')
FONT_NEVIS = __fontdir.format(__actualpath, 'nevis')
FONT_FUNSIZED = __fontdir.format(__actualpath, 'funsized')
FONT_FORTNITE = __fontdir.format(__actualpath, 'fortnite')
FONT_ZOMBIE = __fontdir.format(__actualpath, 'zombie')
FONT_XEN_GALAXIE = __fontdir.format(__actualpath, 'xen_galaxy')
