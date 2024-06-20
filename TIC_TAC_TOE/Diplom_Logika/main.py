import pygame

import modules.background as m_background

import modules.click_handler as m_handler
import modules.button as m_button
pygame.init()
screen_game_width = 680 #225
screen_game_height = 905 #170
screen_game = pygame.display.set_mode((screen_game_width, screen_game_height))

m_background.background.blit_sprite(screen_game)
game = True
FPS = pygame.time.Clock()
m_button.button.blit_sprite(screen_game=screen_game)
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            m_handler.click_cell(pygame.mouse.get_pos(),screen_game)


    
    FPS.tick(50)
    
    
    pygame.display.flip()

