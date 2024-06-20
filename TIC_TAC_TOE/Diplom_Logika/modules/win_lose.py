import pygame
import modules.data_base as m_data
import modules.create_zero as m_zero, modules.create_cross as m_cross
pygame.init()
def win_help(cell,cell1,cell2,screen):
    if m_data.list_cell[cell[0]]==1:
        sim = m_cross.Cross
        name="cross_win"
    else:
        sim = m_zero.Zero
        name="zero_win"
    sim(cell[1],cell[2],name).blit_sprite(screen_game=screen)
    sim(cell1[1],cell1[2],name).blit_sprite(screen_game=screen)
    sim(cell2[1],cell2[2],name).blit_sprite(screen_game=screen)
    m_data.win=True
def win(screen):
    
    if m_data.list_cell[0] == m_data.list_cell[1]== m_data.list_cell[2]!=2:
        win_help([0,0,0],[1,225,0],[2,450,0],screen)
    if m_data.list_cell[3] == m_data.list_cell[4]== m_data.list_cell[5]!=2:
        win_help([3,0,225],[4,225,225],[5,450,225],screen)
    if m_data.list_cell[6] == m_data.list_cell[7]== m_data.list_cell[8]!=2:
        win_help([6,0,450],[7,225,450],[8,450,450],screen)
        
    if m_data.list_cell[0] == m_data.list_cell[3] == m_data.list_cell[6]!=2:
        win_help([0,0,0],[3,0,225],[6,0,450], screen)
    if m_data.list_cell[1] == m_data.list_cell[4] == m_data.list_cell[7]!=2:
        win_help([1,225,0],[4,225,225],[7,225,450], screen)
    if m_data.list_cell[2] == m_data.list_cell[5] == m_data.list_cell[8]!=2:
        win_help([2,450,0],[5,450,225],[8,450,450], screen)

    if m_data.list_cell[0] == m_data.list_cell[4] == m_data.list_cell[8]!=2:
        win_help([0,0,0],[4,225,225],[8,460,450], screen)
    if m_data.list_cell[2] == m_data.list_cell[4] == m_data.list_cell[6]!=2:
        win_help([2,450,0], [4,225,225],[6,0,450], screen)