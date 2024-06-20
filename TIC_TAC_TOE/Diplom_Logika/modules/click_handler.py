import pygame
import modules.data_base as m_data
import modules.create_cross as m_cross, modules.create_zero as m_zero
import modules.win_lose as win_lose
import modules.restart as m_restart
pygame.init()

# pygame.draw.line(surface=screen,color=(250,0,0),start_pos=(0,0),end_pos=(100,100))
def draw(cell, x, y, screen):
    m_data.list_cell[cell] = m_data.step
    
    if m_data.step:
        m_cross.Cross(x,y).blit_sprite(screen)
    else:
        m_zero.Zero(x,y).blit_sprite(screen)
    m_data.step=not m_data.step


def click_cell(cor,screen):
    if not m_data.win:
        if 225> cor[1]> 0:
            if 225>cor[0]> 0 and m_data.list_cell[0]==2:draw(0, x = 0, y = 0, screen=screen)
            elif 450>cor[0]> 225 and m_data.list_cell[1]==2:draw(1, x = 225, y = 0, screen=screen)
            elif 675>cor[0]> 450 and m_data.list_cell[2]==2:draw(2, x = 450, y = 0, screen=screen)
        elif 450> cor[1]> 225:
            if 225> cor [0]> 0 and m_data.list_cell[3]==2:draw(3, x = 0, y = 225, screen=screen)
            elif 450> cor[0]> 0 and m_data.list_cell[4]==2:draw(4, x = 225, y = 225, screen=screen)
            elif 675> cor[0]> 0 and m_data.list_cell[5]==2:draw(5, x = 450, y = 225, screen=screen)
        elif 675>cor[1]> 450:
            if 225>cor[0]>0 and m_data.list_cell[6]==2:draw(6, x = 0, y = 450, screen=screen)
            elif 450>cor[0]>0 and m_data.list_cell[7]==2:draw(7, x = 225, y = 450, screen=screen)
            elif 675>cor[0]> 0 and m_data.list_cell[8]==2:draw(8, x = 450, y = 450, screen=screen)
        win_lose.win(screen)
    if 905>cor[1]>680:
        m_restart.restart(screen)