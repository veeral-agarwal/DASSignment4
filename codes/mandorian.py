import colorama
import numpy as np
import time
dimx = 10000
dimy = 62
colorama.init()

class person:
    def __init__(self,lives=5):
        self.__lives = lives
        
class hero(person):
    def __init__(self):
        super().__init__(self)
        self.__lives = 5 
        self.__score = 0
        self.__tim = 200
        self.__powerup = 1
        self.__sheilds = 3 
        self.__power = 300
        self.__activatedtim = 260
        self.__sheild = False
        self.__shape = [[" ",colorama.Fore.CYAN+"0"+colorama.Fore.RESET,""],
                      ["(","|",")"],
                      ["/"," ","\\"]]
        self.__allowed_collision = [" ","$"]
        self.__collision = ["\\","/","-","|w"]
    def view(self):
        shape = self.__shape
        for i in range(0,3):
            for j in range(0,3):
                print(shape[i][j],end="")
            print()

    def startpostion(self,grid):
        shape = self.__shape
        for i in range(20,23):
            for j in range(dimy-6,dimy-3):
                grid.update_pos(j-30,i+36,shape[i-20][j-dimy+6])

    def place(self,x,y):
        shape = self.__shape
        tempx=-1
        tempy=-1
        for j in range(x,x+3):
            tempy+=1
            tempx=-1
            for i in range(y,y+3):
                tempx+=1
                print("\033["+str(i)+";"+str(j)+"H",end="")
                print(shape[tempx][tempy],end=" ")
            print()
        print("\033["+str(dimy)+";1H")

    def remove(self,x,y):
        shape = self.__shape
        tempx=-1
        tempy=-1
        for j in range(x,x+3):
            tempy+=1
            tempx=-1
            for i in range(y,y+3):
                tempx+=1
                print("\033["+str(i)+";"+str(j)+"H",end="")
                print(" ",end=" ")
            print()
        print("\033["+str(dimy)+";1H")

    def activate_shield(self,x,y):
        if self.__sheilds!=0 and self.__activatedtim-self.__tim>60 :
            self.__sheild=True
            self.__shape = [[colorama.Fore.YELLOW+"/"+colorama.Fore.RESET,colorama.Fore.CYAN+"0 "+colorama.Fore.RESET,colorama.Fore.YELLOW+"\\"+colorama.Fore.RESET],
                        [colorama.Fore.YELLOW+"|"+colorama.Fore.RESET,"|",colorama.Fore.YELLOW+"|"+colorama.Fore.RESET],
                        [colorama.Fore.YELLOW+"\\"+colorama.Fore.RESET," ",colorama.Fore.YELLOW+"/"+colorama.Fore.RESET]]
            self.remove(x,y)
            self.place(x,y)
            self.__sheilds-=1
            self.__activatedtim = self.__tim

    def lives(self):
        if self.__lives>=0:
            shape = ["L","I","V","E","S"," ",":"," ",str(self.__lives)]
            tempx=-1
            for i in shape:
                tempx+=1
                print("\033["+str(1)+";"+str(1+tempx)+"H",end="")
                print(i,end="")
            print("\033["+str(dimy)+";1H")

    def score(self):
        a = str(self.__score)+"  "
        shape = ["S","C","O","R","E"," ",":"," ",a]
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(1)+";"+str(20+tempx)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")

    def shield(self,x,y):
        sample= str(self.__activatedtim-self.__tim)+"  "
        if self.__sheild:
            sample=0
        shape = ["S","H","I","E","L","D"," ",":"," ",str(self.__sheilds)," ",str(sample)]
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(1)+";"+str(60+tempx)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")
        if(self.__activatedtim-self.__tim>10):
            self.__shape = [[" ",colorama.Fore.CYAN+"0"+colorama.Fore.RESET,""],
                      ["(","|",")"],
                      ["/"," ","\\"]]
            self.remove(x,y)
            self.place(x,y)
            self.__sheild = False

    def countdown(self):
        check = str(self.__tim)+"  " 
        shape = ["T","I","M","E","R"," ",":"," ",check]
        tempx=-1
        for i in shape:
            tempx+=1
            print("\033["+str(1)+";"+str(40+tempx)+"H",end="")
            print(i,end="")
        print("\033["+str(dimy)+";1H")
        if self.__tim<90:
            print("\033["+str(1)+";"+str(50)+"H",end="")
            print(" ",end="")
            print("\033["+str(dimy)+";1H")

    def update_tim(self):
        self.__tim-=1

    def show_tim(self):
        return self.__tim

    def update_score(self,penalty=5):
        self.__score+=penalty

    def hit_zap(self):
        self.__score-=10
        self.__lives-=1
        if self.__lives==0:
            print("Game Over")
            exit(1)
    
    def is_sheield_active(self):
        return self.__sheild

    def quick(self):
        if self.__powerup>0 :
            self.__power=self.__tim
            self.__powerup-=1
            return True
        else:
            return False
    def quick_check(self):
        if self.__power - self.__tim < 10 and self.__power-self.__tim >=0:
            return True
        return False
class bullet:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.__shape = ["=",">"]

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
        if(self.__x<=212):
            self.__x+=check
        else:
            return True
            
    def position(self):
        coordinates = [self.__x,self.__y]
        return coordinates