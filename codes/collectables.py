import random
import colorama as col
dimx = 10000
dimy = 62
col.init()

class collect:
    def __init__(self,x,y):
        self.__score = 15
        self.__shape = []
        self.__hit = False
        self.__x = x
        self.__y = y
    def destroy(self):
        self.__hit = True   
        self.__shape=[]

class coin(collect):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.__shape=[col.Fore.YELLOW+"$"+col.Fore.RESET]
        self.__score = 10
        self.__x = x
        self.__y =y
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
        if(self.__x>0):
            self.__x-=check
        else:
            return True
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates 