import pygame
from settings import Settings
from mole import Mole
from hole import Hole

def run_game():
    gm_set = Settings()
    pygame.init()
    mole = Mole(150, 75)
    
    holes = [
        Hole(150, 475),
        Hole(150, 275),
        Hole(150, 75),
        Hole(450, 475),
        Hole(450, 275),
        Hole(450, 75),
        Hole(750, 475),
        Hole(750, 275),
        Hole(750, 75),
    ]

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

        for hole in holes:
            hole.draw(screen)
    
        pygame.display.update()
        pygame.display.flip()


        Clock.tick(60)

run_game()
