import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self, wx):
        super().__init__()
        all_Sprite_List.add(self)
        walls.add(self)
        self.image = pygame.Surface((1,30))
        self.rect = Rect = Rect(wx[0], wx[1], 1, 30)

    #for Wall in walls:
        #if pygame.sprite.collide_rect(self, wall):
            #if px > 0:
                #self.rect.right = wall.rect.left
            #if px < 0:
                #self.rect.left = wall.rect.right
