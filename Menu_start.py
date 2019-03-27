from tkinter import Tk, PhotoImage, Canvas
import sys,os
from tkinter import *
sys.path.append ("../")                                                                     #donne le chemin pour nos bibliothèques perso
import parallax
#import choix
import Pygame
#------------------------------------------------------------ Création de la fenetre Tkinter -----------------------------------------------------------------------------------------------
class Interface(Tk):
    def __init__(self, path_image):
        super(Interface, self).__init__()
        self.title("PlatformZ")
        self.attributes("-fullscreen", 1)
        self.image = PhotoImage(file=path_image)
        self.w, self.h = self.image.width(), self.image.height()
        self.canvas = Canvas(self, width=self.w, height=self.h)
        self.canvas.pack()
        self.canvas.create_image((self.w//2, self.h//2), image=self.image)
        commencer = Button(self,text='Commencer',command=Pygame.gameloop).place(x='1210',y='360')  #Crée et place un bouton qui lance le jeu
        quitter = Button(self,text='Quitter',command=self.quit).place(x='1225',y='400')
        self.mainloop()
#------------------------------------------------------------- Appel de fonction -----------------------------------------------------------------------------------------------------------
Interface("./assets/images/fond/background.png")
