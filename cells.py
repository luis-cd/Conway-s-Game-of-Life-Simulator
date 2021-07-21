import pygame
import numpy as np
import gamefunctions as gf


class Cell():

    def __init__(self,cw_settings):
        '''Initialize cell class'''
        self.width,self.height = cw_settings.width, cw_settings.height
        self.nxC,self.nyC= cw_settings.numberx,cw_settings.numbery
        self.dimCW = self.width / self.nxC
        self.dimCH = self.height / self.nyC
        self.gameState=np.zeros((self.nxC,self.nyC),int) #Valores numéricos asociados a cada celda.
        self.gameState[1,0:3]=1


    def check_neighbours(self, x,y):
        '''Check the state of closer neighbours and return the state of the cell in the next t.'''
        n_neigh=(self.gameState[(x+1)%self.nxC,(y+1)%self.nyC ] 
            +         self.gameState[(x+1)%self.nxC,(y-1)%self.nyC]
            +         self.gameState[(x+1)%self.nxC,y %self.nyC] 
            +         self.gameState[x%self.nxC,(y-1)%self.nyC] 
            +         self.gameState[(x-1)%self.nxC,(y-1)%self.nyC]
            +         self.gameState[(x-1)%self.nxC,y%self.nyC] 
            +         self.gameState[(x-1)%self.nxC,(y+1)%self.nyC] 
            +         self.gameState[x%self.nxC,(y+1)%self.nyC])


        if self.gameState[x, y] == 1 and n_neigh in [2, 3]:
            return 1

        elif self.gameState[x,y]==0 and n_neigh==3:
            return 1

        else:
            return 0


    def update_cells(self,cw_settings,screen):
        '''Update the cells'''
        self.nextGameState=np.zeros((self.nxC,self.nyC))
        for x in range(self.nyC):
            for y in range(self.nxC):
                poly=[(x*self.dimCW,   y*self.dimCH),
                ((x+1)*self.dimCW,      y*self.dimCH),
                ((x+1)*self.dimCW,    (y+1)*self.dimCH),
                (x*self.dimCW,          (y+1)*self.dimCH)]

                self.nextGameState[x,y]=self.check_neighbours(x,y)

                if self.nextGameState[x,y]==0:
                    pygame.draw.polygon(screen, (128,128,128),poly,1)

                elif self.nextGameState[x,y]==1:
                    pygame.draw.polygon(screen, (230,230,230),poly,0)

        del self.gameState
        self.gameState=self.nextGameState.copy()
