import sys
import pygame
import numpy as np

def set_screen(cw_settings):
    '''Creates the initial screen settings and return the object for screen.'''
    width,height = cw_settings.width, cw_settings.height
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption('Conway\'s life game')
    return screen

def cover_screen(cw_settings,screen):
    '''Cover the screen to erase the previous configuration.'''
    bg=cw_settings.bg
    screen.fill((bg))

def get_mouse_pos(cw_settings):
    '''Return the cell where you're clicking.'''
    dimCW = cw_settings.width / cw_settings.numberx
    dimCH = cw_settings.height / cw_settings.numbery
    (posx,posy)=pygame.mouse.get_pos()
    cellx=int(np.floor(posx/dimCW))
    celly=int(np.floor(posy/dimCH))
    return cellx,celly

def change_cell_state(cw_settings,cells):  
    mouseClick=pygame.mouse.get_pressed()
    if sum(mouseClick)>0:
        print('ok')
        cellx,celly=get_mouse_pos(cw_settings)
        cells.nextGameState[cellx,celly]=int(not cells.gameState[cellx,celly])

def check_events(cw_settings,cells):
    '''Check for all kinds of events.'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    cw_settings.pauseState=not cw_settings.pauseState
        

def update_screen(cw_settings,screen,cells):
    cells.update_cells(cw_settings,screen)
    pygame.display.flip()
