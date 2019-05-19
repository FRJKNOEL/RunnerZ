import pygame

class Balle(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        self.sheet = pygame.image.load('./assets/images/balle.png')
        self.sheet.set_clip(pygame.Rect(0, 4, 22, 4))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 4, 22, 4)}#, 1: (0, 4, 44, 4) }
        self.right_states = { 0: (0, 0, 22, 4)}#, 1: (0, 0, 44, 4) }
        self.life = 1
        self.direction = direction

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
       
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 8
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 8
 
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
 
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
        
        if self.direction =='right':
            self.update('right')
