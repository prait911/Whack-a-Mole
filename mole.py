import pygame

class Mole:
    def __init__(self, x, y):
        self.image = pygame.image.load("mole.png")
        self.small_mole = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.small_mole.get_rect()
        self.rect.topleft = (x, y)
        

    def draw(self, screen):
        screen.blit(self.small_mole, self.rect)
        



        


