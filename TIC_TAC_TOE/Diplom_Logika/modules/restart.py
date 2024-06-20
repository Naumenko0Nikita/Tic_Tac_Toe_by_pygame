import pygame
import modules.data_base as m_data 
import modules.background as m_background
def restart(screen_game):
    m_data.list_cell=[2,2,2,
                      2,2,2,
                      2,2,2]
    m_data.win=False
    m_background.background.blit_sprite(screen_game)
    m_data.step=not m_data.step