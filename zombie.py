import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('./assets/images/personnages/zombie.png')
        self.sheet.set_clip(pygame.Rect(0, 76, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (104, 76, 52, 76), 3: (156, 76, 52, 76), 4: (208, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (104, 152, 52, 76), 3: (156, 152, 52, 76), 4:(208, 152, 52, 76) }
        self.life = 1


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
            self.rect.x -= 3
        elif direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 3
 
        elif direction == 'stand_left':
            self.clip(self.left_states[0])
        elif direction == 'stand_right':
            self.clip(self.right_states[0])
            
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        direction = 'left'
        
        if direction =='left':
            self.update('left')

        '''
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_j:
                self.update('left')
            if event.key == pygame.K_l:
                self.update('right')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_j:
                self.update('stand_left')            
            if event.key == pygame.K_l:
                self.update('stand_right')
        '''
