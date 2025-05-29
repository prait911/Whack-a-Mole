import pygame


class Hole:
    def __init__(self, x, y):
        self.hole = pygame.image.load("hole2.png")
        self.small_hole = pygame.transform.scale(self.hole, (150, 150))
        self.rect = self.small_hole.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.small_hole, self.rect)
        
    
