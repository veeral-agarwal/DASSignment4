import random
import colorama
import numpy as np
from mandorian import hero 
colorama.init()
ground = colorama.Fore.GREEN+"X"+colorama.Fore.RESET
top = colorama.Fore.BLUE+"^"
dimx = 10000
dimy = 62

class aren:
    def __init__(self):
        dummy = []
        for i in range(dimx):
            dummy.append([])
            for j in range(dimy):
                dummy[i].append(" ")
        self.__grid = dummy

    def add_gound(self):
        for i in range(0,dimx):
            self.__grid[i][dimy-1] = ground
            self.__grid[i][dimy-2] = ground
            self.__grid[i][dimy-3] = ground

    def add_top(self):
        for i in range(dimx):
            self.__grid[i][1]=top
    
    def print_grid(self,corx,cory):
        area = self.__grid
        for j in range(dimy):
            for i in range(corx,corx+212):
                print(area[i][j],end='')
            print()
            
    def update_pos(self,x,y,char):
        self.__grid[x][y]=char