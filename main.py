import pygame
from settings import Settings
from mole import Mole

def run_game():
    gm_set = Settings()
    pygame.init()
    mole = Mole(100, 100)

    screen = pygame.display.set_mode((gm_set.screen_width, gm_set.screen_height))
    pygame.display.set_caption(gm_set.caption)

    
    screen.fill(gm_set.bg_color)
    Clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        mole.draw(screen)
    
        pygame.display.update()
        pygame.display.flip()


        Clock.tick(60)

run_game()
