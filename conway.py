import pygame
import gamefunctions as gf
from time import sleep
from settings import Settings
from cells import Cell
#---------------------------------------------------------------------------------------------------

cw_settings=Settings()

pygame.init()  #Creation of screen and stuff.
screen=gf.set_screen(cw_settings)
cells=Cell(cw_settings)


if __name__=='__main__':   
    '''Initialize the game'''
    while True:
        '''Loop for the game action.'''
        gf.check_events(cw_settings,cells)
        gf.cover_screen(cw_settings,screen)
        gf.update_screen(cw_settings,screen,cells)
        sleep(cw_settings.timeSleep)