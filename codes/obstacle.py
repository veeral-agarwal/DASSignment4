import random
import colorama as col
import numpy as np
dimx = 10000
dimy = 62
col.init()
class obstacle:
    def __init__(self,x,y):
        self.__penalty=10
        self.__score = 15
        self.__shape = []
        self.__hit = False
        self.__x = x
        self.__y = y
    def destroy(self):
        self.__hit = True   
        self.__shape=[]

class zapper_horizontal(obstacle):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.__shape=[col.Fore.WHITE+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET,
        col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET
        ,col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET,
        col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET,
        col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET,col.Fore.RED+"-"+col.Fore.RESET
        ,col.Fore.WHITE+"-"+col.Fore.RESET]
        self.__x = x
        self.__y = y
    def place(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y)+";"+str(x+tempx)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")
    def remove(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y)+";"+str(x+tempx)+"H",end="")
            print(" ",end="")
        print("\033["+str(dimy)+";1H")
    def update(self,check=1):
        if(self.__x>2):
            self.__x-=check
        else:
            return True
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates        
class zapper_verticle(obstacle):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.__shape=[col.Fore.WHITE+"|"+col.Fore.RESET,col.Fore.RED+"|"+col.Fore.RESET,
        col.Fore.RED+"|"+col.Fore.RESET,col.Fore.RED+"|"+col.Fore.RESET,col.Fore.RED+"|"+col.Fore.
        RESET,col.Fore.RED+"|"+col.Fore.RESET,col.Fore.RED+"|"+col.Fore.RESET,
        col.Fore.RED+"|"+col.Fore.RESET,col.Fore.WHITE+"|"+col.Fore.RESET]
        self.__x = x
        self.__y = y
    def place(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y+tempx)+";"+str(x)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")
    def remove(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y+tempx)+";"+str(x)+"H",end="")
            print(" ",end="")
        print("\033["+str(dimy)+";1H")
    def update(self,check=1):
        if(self.__x>2):
            self.__x-=check
        else:
            return True
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates        
class zapper_cross(obstacle):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.__shape=[col.Fore.WHITE+"\\"+col.Fore.RESET,col.Fore.RED+"\\"+col.Fore.RESET,
        col.Fore.RED+"\\"+col.Fore.RESET,col.Fore.RED+"\\"+col.Fore.RESET,
        col.Fore.RED+"\\"+col.Fore.RESET,col.Fore.WHITE+"\\"+col.Fore.RESET]
        self.__x = x
        self.__y = y
    def place(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        temp=-1
        for i in shape:
            temp+=1
            print("\033["+str(y+temp)+";"+str(x+temp)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")  
    def remove(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        temp=-1
        for i in shape:
            temp+=1
            print("\033["+str(y+temp)+";"+str(x+temp)+"H",end="")
            print(" ",end="")
        print("\033["+str(dimy)+";1H")
    def update(self,check=1):
        if(self.__x>2):
            self.__x -=check
        else:
            return True
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates 
class magnet(obstacle):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.__shape=[col.Fore.WHITE+"|"+col.Fore.RESET,col.Fore.WHITE+"|"+col.Fore.RESET,
        col.Fore.LIGHTWHITE_EX+"="+col.Fore.WHITE,col.Fore.RED+"M"+col.Fore.RED,
        col.Fore.LIGHTWHITE_EX+"="+col.Fore.WHITE,col.Fore.WHITE+"|"+col.Fore.RESET,
        col.Fore.WHITE+"|"+col.Fore.RESET]
        self.__x = x
        self.__y = y
    def place(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y)+";"+str(x+tempx)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")  
    def remove(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y)+";"+str(x+tempx)+"H",end="")
            print(" ",end="")
        print("\033["+str(dimy)+";1H")
    def update(self,check =1):
        if(self.__x>2):
            self.__x -=check
        else:
            return True
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates 
class boss(obstacle):
    def __init__(self,x,y):
        super().__init__(x,y)
        shape=[]
        coord = []
        with open("./drag") as obj:
            i=0
            for line in obj:
                for j in range(len(line)):
                    if line[j] != ' ':
                        shape.append(line[j])
                        coord.append([i+x,j+y])
                i+=1
        self.__shape = shape
        self.__coord = np.array(coord)
        self.__x = x
        self.__y = y
        self.__lives = 9
    def place(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        coord = self.__coord
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(coord[tempx][0])+";"+str(coord[tempx][1])+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")
    def remove(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        coord = self.__coord
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(coord[tempx][0])+";"+str(coord[tempx][1])+"H",end="")
            print(" ",end="")
        print("\033["+str(dimy)+";1H")
    def update(self,coordinates):
        coord = self.__coord
        if(coordinates[1]-coord[0][0]==11):
            return True
        elif (coordinates[1]-coord[0][0]<11):
            if self.__coord[0,0]>3:
                self.__coord[:,0]=self.__coord[:,0]-1
                return True
        elif (coordinates[1]-coord[0][0]>-11):
            if self.__coord[0,0]<46:
                self.__coord[:,0]=self.__coord[:,0]+1
                return True
        return True
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates
    def lives(self):
        if self.__lives>=0:
            shape = ["B","O","S","S"," ",":"," ",str(self.__lives)]
            tempx=-1
            for i in shape:
                tempx+=1
                print("\033["+str(1)+";"+str(80+tempx)+"H",end="")
                print(i,end="")
            print("\033["+str(dimy)+";1H")
        else:
            shape = [" "," "," "," "," "," "," "," "," "," "," "]
            tempx=-1
            for i in shape:
                tempx+=1
                print("\033["+str(1)+";"+str(80+tempx)+"H",end="")
                print(i,end="")
            print("\033["+str(dimy)+";1H")
    def shot(self):
        self.__lives-=1
    def dead(self):
        if self.__lives<=0:
            return True
        return False
class ball(obstacle):
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__shape = ["<","="]

    def place(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y)+";"+str(x+tempx)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")

    def remove(self):
        x = self.__x
        y = self.__y
        shape = self.__shape
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(y)+";"+str(x+tempx)+"H",end="")
            print(" ",end="")
        print("\033["+str(dimy)+";1H")

    def update(self,check = 1):
        if(self.__x>2):
            self.__x-=check
        else:
            return True
            
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates