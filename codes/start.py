from arena import aren
from mandorian import hero,bullet
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from obstacle import obstacle,zapper_horizontal,zapper_verticle,zapper_cross,magnet,boss,ball
from collectables import coin
import time
import os
import math
import signal
import random
import colorama

colorama.init()
xcoor = 1
ycoor = 57
coordinates = [xcoor,ycoor]
zappers = []
coins = []
magnets = []
bullets = []
balls = []
gra = [1]
present=[time.time()]

gr = aren()
gr.add_gound()
gr.add_top()
mand = hero()
gr.print_grid(0,0)
mand.place(xcoor,ycoor)
bos = boss(46,172)

def alarmhandler(signum, frame):
    raise AlarmException
def user_input(timeout=0.15):
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    
    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
def gravity(coordinates,gra):
    if(coordinates[1]<10):
        mand.remove(coordinates[0],coordinates[1])
        coordinates[1]+=1
        mand.place(coordinates[0],coordinates[1])
    elif(coordinates[1]+gra[0]<57):
        mand.remove(coordinates[0],coordinates[1])
        coordinates[1]=math.floor(gra[0]+coordinates[1])
        gra[0]=gra[0]+0.06
        mand.place(coordinates[0],coordinates[1])
    elif coordinates[1]<57:
        mand.remove(coordinates[0],coordinates[1])
        coordinates[1]=57
        gra[0]=1
        mand.place(coordinates[0],coordinates[1])
    else:
        gra[0]=1
    return coordinates,gra
def collision(coordinates,zappers,coins,magnets,balls):
    for i in coins:
        coord = i.position()
        if(coordinates[0]==coord[0] and coordinates[1]==coord[1] 
        or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]
        or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]
        or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]
        or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]
        or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]
        or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]
        or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]
        or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]):
            mand.update_score()
            i.remove()
            coins.remove(i)
    if not mand.is_sheield_active():
        for i in magnets:
            coord = i.position()
            if(coordinates[1]==coord[1] or coordinates[1]+2==coord[1]):
                mand.remove(coordinates[0],coordinates[1])
                coordinates[0]=coord[0]+2
                coordinates[1]= coord[1]
                mand.place(coordinates[0],coordinates[1])
                mand.update_score(-15)
        if coordinates[0]>=172 and coordinates[1]-bos.position()[0]<=10 and coordinates[1]-bos.position()[0]>=0 and mand.show_tim()<90:
            mand.hit_zap()
    for i in zappers:
        if(i[0]==1):
            coord = i[1].position()
            if(coordinates[0]==coord[0] and coordinates[1]==coord[1] 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+1 and coordinates[1]==coord[1]+1 
            or coordinates[0]+1==coord[0]+1 and coordinates[1]==coord[1]+1
            or coordinates[0]+2==coord[0]+1 and coordinates[1]==coord[1]+1
            or coordinates[0]+2==coord[0]+1 and coordinates[1]+1==coord[1]+1
            or coordinates[0]+2==coord[0]+1 and coordinates[1]+2==coord[1]+1
            or coordinates[0]+1==coord[0]+1 and coordinates[1]+2==coord[1]+1
            or coordinates[0]==coord[0]+1 and coordinates[1]+2==coord[1]+1
            or coordinates[0]==coord[0]+1 and coordinates[1]+1==coord[1]+1
            or coordinates[0]+1==coord[0]+1 and coordinates[1]+1==coord[1]+1
            
            or coordinates[0]==coord[0]+2 and coordinates[1]==coord[1]+2 
            or coordinates[0]+1==coord[0]+2 and coordinates[1]==coord[1]+2
            or coordinates[0]+2==coord[0]+2 and coordinates[1]==coord[1]+2
            or coordinates[0]+2==coord[0]+2 and coordinates[1]+1==coord[1]+2
            or coordinates[0]+2==coord[0]+2 and coordinates[1]+2==coord[1]+2
            or coordinates[0]+1==coord[0]+2 and coordinates[1]+2==coord[1]+2
            or coordinates[0]==coord[0]+2 and coordinates[1]+2==coord[1]+2
            or coordinates[0]==coord[0]+2 and coordinates[1]+1==coord[1]+2
            or coordinates[0]+1==coord[0]+2 and coordinates[1]+1==coord[1]+2
            
            or coordinates[0]==coord[0]+3 and coordinates[1]==coord[1]+3 
            or coordinates[0]+1==coord[0]+3 and coordinates[1]==coord[1]+3
            or coordinates[0]+2==coord[0]+3 and coordinates[1]==coord[1]+3
            or coordinates[0]+2==coord[0]+3 and coordinates[1]+1==coord[1]+3
            or coordinates[0]+2==coord[0]+3 and coordinates[1]+2==coord[1]+3
            or coordinates[0]+1==coord[0]+3 and coordinates[1]+2==coord[1]+3
            or coordinates[0]==coord[0]+3 and coordinates[1]+2==coord[1]+3
            or coordinates[0]==coord[0]+3 and coordinates[1]+1==coord[1]+3
            or coordinates[0]+1==coord[0]+3 and coordinates[1]+1==coord[1]+3
            
            or coordinates[0]==coord[0]+4 and coordinates[1]==coord[1]+4 
            or coordinates[0]+1==coord[0]+4 and coordinates[1]==coord[1]+4
            or coordinates[0]+2==coord[0]+4 and coordinates[1]==coord[1]+4
            or coordinates[0]+2==coord[0]+4 and coordinates[1]+1==coord[1]+4
            or coordinates[0]+2==coord[0]+4 and coordinates[1]+2==coord[1]+4
            or coordinates[0]+1==coord[0]+4 and coordinates[1]+2==coord[1]+4
            or coordinates[0]==coord[0]+4 and coordinates[1]+2==coord[1]+4
            or coordinates[0]==coord[0]+4 and coordinates[1]+1==coord[1]+4
            or coordinates[0]+1==coord[0]+4 and coordinates[1]+1==coord[1]+4
            
            or coordinates[0]==coord[0]+5 and coordinates[1]==coord[1]+5 
            or coordinates[0]+1==coord[0]+5 and coordinates[1]==coord[1]+5
            or coordinates[0]+2==coord[0]+5 and coordinates[1]==coord[1]+5
            or coordinates[0]+2==coord[0]+5 and coordinates[1]+1==coord[1]+5
            or coordinates[0]+2==coord[0]+5 and coordinates[1]+2==coord[1]+5
            or coordinates[0]+1==coord[0]+5 and coordinates[1]+2==coord[1]+5
            or coordinates[0]==coord[0]+5 and coordinates[1]+2==coord[1]+5
            or coordinates[0]==coord[0]+5 and coordinates[1]+1==coord[1]+5
            or coordinates[0]+1==coord[0]+5 and coordinates[1]+1==coord[1]+5):
                i[1].remove()
                zappers.remove(i)
                if not mand.is_sheield_active():
                    mand.hit_zap()
        elif i[0]==2:
            coord = i[1].position()
            if(coordinates[0]==coord[0] and coordinates[1]==coord[1] 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+1 and coordinates[1]==coord[1] 
            or coordinates[0]+1==coord[0]+1 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+1 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+1 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+1 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+1 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+1 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+1 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+1 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+2 and coordinates[1]==coord[1] 
            or coordinates[0]+1==coord[0]+2 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+2 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+2 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+2 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+2 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+2 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+2 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+2 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+3 and coordinates[1]==coord[1] 
            or coordinates[0]+1==coord[0]+3 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+3 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+3 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+3 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+3 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+3 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+3 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+3 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+4 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+4 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+4 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+4 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+4 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+4 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+4 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+4 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+4 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+5 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+5 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+5 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+5 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+5 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+5 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+5 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+5 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+5 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+6 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+6 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+6 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+6 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+6 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+6 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+6 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+6 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+6 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+7 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+7 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+7 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+7 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+7 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+7 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+7 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+7 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+7 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+8 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+8 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+8 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+8 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+8 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+8 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+8 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+8 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+8 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+9 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+9 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+9 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+9 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+9 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+9 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+9 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+9 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+9 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+10 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+10 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+10 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+10 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+10 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+10 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+10 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+10 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+10 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+11 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+11 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+11 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+11 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+11 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+11 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+11 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+11 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+11 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+12 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+12 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+12 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+12 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+12 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+12 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+12 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+12 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+12 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+13 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+13 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+13 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+13 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+13 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+13 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+13 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+13 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+13 and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0]+14 and coordinates[1]==coord[1]
            or coordinates[0]+1==coord[0]+14 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+14 and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0]+14 and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0]+14 and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0]+14 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+14 and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0]+14 and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0]+14 and coordinates[1]+1==coord[1]):
                i[1].remove()
                zappers.remove(i)
                if not mand.is_sheield_active():
                    mand.hit_zap()
        elif i[0]==3:
            coord = i[1].position()
            if(coordinates[0]==coord[0] and coordinates[1]==coord[1] 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]
            
            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+1 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+1
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+1
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+1
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+1
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+1
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+1
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+1
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+1
            
            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+2 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+2
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+2
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+2
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+2
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+2
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+2
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+2
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+2
            
            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+3 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+3
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+3
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+3
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+3
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+3
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+3
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+3
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+3
            
            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+4 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+4
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+4
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+4
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+4
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+4
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+4
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+4
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+4
            
            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+5
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+5
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+5
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+5
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+5
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+5
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+5
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+5
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+5

            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+6 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+6
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+6
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+6
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+6
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+6
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+6
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+6
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+6
            
            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+7 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+7
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+7
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+7
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+7
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+7
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+7
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+7
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+7
            
            or coordinates[0]==coord[0] and coordinates[1]==coord[1]+8 
            or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]+8
            or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]+8
            or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]+8
            or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]+8
            or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]+8
            or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]+8
            or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]+8
            or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]+8):
                i[1].remove()
                zappers.remove(i)
                if not mand.is_sheield_active():
                    mand.hit_zap()
    for i in balls:
        coord = i.position()
        if(coordinates[0]==coord[0] and coordinates[1]==coord[1] 
        or coordinates[0]+1==coord[0] and coordinates[1]==coord[1]
        or coordinates[0]+2==coord[0] and coordinates[1]==coord[1]
        or coordinates[0]+2==coord[0] and coordinates[1]+1==coord[1]
        or coordinates[0]+2==coord[0] and coordinates[1]+2==coord[1]
        or coordinates[0]+1==coord[0] and coordinates[1]+2==coord[1]
        or coordinates[0]==coord[0] and coordinates[1]+2==coord[1]
        or coordinates[0]==coord[0] and coordinates[1]+1==coord[1]
        or coordinates[0]+1==coord[0] and coordinates[1]+1==coord[1]):
            if not mand.is_sheield_active():
                mand.hit_zap()
            i.remove()
            balls.remove(i)
    return coordinates,zappers,coins,magnets,balls   
def make_zappers_cross(zappers):
    zap = zapper_cross(208,random.randint(3,54))
    temp = [1,zap]
    zap.place()
    zappers.append(temp)
    return zappers
def make_zappers_horizontal(zappers):
    zap = zapper_horizontal(199,random.randint(3,57))
    zap.place()
    temp = [2,zap]
    zappers.append(temp)
    return zappers
def make_zappers_verticle(zappers):
    zap = zapper_verticle(208,random.randint(3,51))
    zap.place()
    temp = [3,zap]
    zappers.append(temp)
    return zappers
def make_magnet(magnets):
    mag = magnet(206,random.randint(3,57))
    mag.place()
    magnets.append(mag)
    return magnets
def make_coins(coins):
    t = random.randint(3,57)
    coi = coin(208,t)
    coi.place()
    coins.append(coi)
    return coins
def movement(coordinates,zappers,coins,magnets,bullets):
    for i in zappers:
        i[1].remove()
        up =1
        if mand.quick_check():
            up = 2
        check = i[1].update(up)
        if(not check):
            i[1].place()
        else:
            zappers.remove(i)
    for i in magnets:
        i.remove()
        up =1
        if mand.quick_check():
            up = 2
        check = i.update(up)
        if(not check):
            i.place()
        else:
            magnets.remove(i)
    for i in coins:
        i.remove()
        up =1
        if mand.quick_check():
            up = 2
        check = i.update(up)
        if(not check):
            i.place()
        else:
            coins.remove(i)
    for i in bullets:
        i.remove()
        up =1
        if mand.quick_check():
            up = 2
        check = i.update(up)
        if(not check):
            i.place()
        else:
            bullets.remove(i)
    for i in balls:
        up =1
        if mand.quick_check():
            up = 2
        i.remove()
        check = i.update(up)
        if(not check):
            i.place()
        else:
            balls.remove(i)
    if(coordinates[0]>2 and mand.show_tim()>90):
        mand.remove(coordinates[0],coordinates[1])
        coordinates[0]-=1
        mand.place(coordinates[0],coordinates[1])
    return coordinates,zappers,coins,magnets
def move(coordinates):
    char =user_input()
    if char == "d":
        if coordinates[0]<208:
            mand.remove(coordinates[0],coordinates[1])
            coordinates[0]+=3
            mand.place(coordinates[0],coordinates[1])
        return coordinates
    elif char =="a":
        if coordinates[0]>2:
            mand.remove(coordinates[0],coordinates[1])
            coordinates[0]-=3
            mand.place(coordinates[0],coordinates[1])
        return coordinates
    elif char=="w":
        if(coordinates[1]>5):
            mand.remove(coordinates[0],coordinates[1])
            coordinates[1]-=3
            mand.place(coordinates[0],coordinates[1])
        return coordinates
    elif char==" ":
        mand.activate_shield(coordinates[0],coordinates[1])
    elif char=="p":
        mand.quick()
    elif char=="b":
        shoot_bullets(coordinates)
    elif char =="q":
        exit(1)
    return coordinates
def update_score(mand):
    mand.lives()
    mand.score()
    mand.countdown()
    mand.shield(coordinates[0],coordinates[1])
    if mand.show_tim()<90:
        bos.lives()
def make_obstacles(coordinates,zappers,coins,magnets):
    if mand.show_tim()>90:
        if(random.random()>0.98):
            make_zappers_cross(zappers)
        if(random.random()>0.98):
            make_zappers_horizontal(zappers)
        if(random.random()>0.98):
            make_zappers_verticle(zappers)
        if(random.random()>0.97):
            make_coins(coins)
        if(random.random()>0.999):
            make_magnet(magnets)
    else:
        boss_movement(coordinates)     
def shoot_bullets(coordinates):
    mand.update_score(-1)
    bul = bullet(coordinates[0]+2,coordinates[1]+1)
    bul.place()
    bullets.append(bul)
def shot_bullets(bullets,zappers,coins,magnets,balls):
    check = bos.position()
    for i in bullets:
        coordinate = i.position()
        if(mand.show_tim()<90):
            if (coordinate[0]==172 and (coordinate[1]-check[0])<8 and coordinate[1]-check[0]>=0):
                i.remove()
                bullets.remove(i)
                bos.shot()
        for j in balls:
            coord = j.position()
            if(coordinate[0]+2==coord[0] and coordinate[1]==coord[1]
            or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]
            or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]):
                j.remove()
                balls.remove(j)
                i.remove()
                bullets.remove(i)
        for j in magnets:
            coord = j.position()
            if(coordinate[0]+2==coord[0] and coordinate[1]==coord[1]
            or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]
            or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]):
                j.remove()
                i.remove()
                bullets.remove(i)
                magnets.remove(j)
                mand.update_score(20)
        for j in zappers:
            coord = j[1].position()
            if(j[0]==1):
                if(coordinate[0]+1==coord[0] and coordinate[1]==coord[1]
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]
                
                or coordinate[0]+1==coord[0]+1 and coordinate[1]==coord[1]+1
                or coordinate[0]+2==coord[0]+1 and coordinate[1]==coord[1]+1
                or coordinate[0]+3==coord[0]+1 and coordinate[1]==coord[1]+1
                
                or coordinate[0]+1==coord[0]+2 and coordinate[1]==coord[1]+2
                or coordinate[0]+2==coord[0]+2 and coordinate[1]==coord[1]+2
                or coordinate[0]+3==coord[0]+2 and coordinate[1]==coord[1]+2
                
                or coordinate[0]+1==coord[0]+3 and coordinate[1]==coord[1]+3
                or coordinate[0]+2==coord[0]+3 and coordinate[1]==coord[1]+3
                or coordinate[0]+3==coord[0]+3 and coordinate[1]==coord[1]+3
                
                or coordinate[0]+1==coord[0]+4 and coordinate[1]==coord[1]+4
                or coordinate[0]+2==coord[0]+4 and coordinate[1]==coord[1]+4
                or coordinate[0]+3==coord[0]+4 and coordinate[1]==coord[1]+4
                
                or coordinate[0]+1==coord[0]+5 and coordinate[1]==coord[1]+5
                or coordinate[0]+2==coord[0]+5 and coordinate[1]==coord[1]+5
                or coordinate[0]+3==coord[0]+5 and coordinate[1]==coord[1]+5):
                    i.remove()
                    bullets.remove(i)
                    zappers.remove(j)
                    j[1].remove()
                    mand.update_score(10)
            elif(j[0]==2):
                if(coordinate[0]+1==coord[0] and coordinate[1]==coord[1]
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]):
                    i.remove()
                    bullets.remove(i)
                    j[1].remove()
                    mand.update_score(10)
                    zappers.remove(j)
            elif(j[0]==3):
                if(coordinate[0]+1==coord[0] and coordinate[1]==coord[1]
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+1
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+1
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+1
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+2
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+2
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+2
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+3
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+3
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+3
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+4
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+4
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+4
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+5
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+5
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+5
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+6
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+6
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+6
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+7
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+7
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+7
                
                or coordinate[0]+1==coord[0] and coordinate[1]==coord[1]+8
                or coordinate[0]+2==coord[0] and coordinate[1]==coord[1]+8
                or coordinate[0]+3==coord[0] and coordinate[1]==coord[1]+8):
                    j[1].remove()
                    i.remove()
                    bullets.remove(i)
                    mand.update_score(10)
                    zappers.remove(j)
    return bullets,zappers,coins,magnets,balls
def shoot_ball(coordinates,bos,balls):
    cord = bos.position()
    bul = ball(171,coordinates[1])
    balls.append(bul)
def countdown(present):
    if(not mand.quick_check()):
        if(time.time()-present[0]>1):
            mand.update_tim()
            present[0]=time.time()
    else:
        if(time.time()-present[0]>0.5):
            mand.update_tim()
            present[0]=time.time()
    return present
def boss_movement(coordinates):
    if not bos.dead():
        if coordinates[1]>10:
            bos.remove()
            if bos.update(coordinates):
                bos.place()
        if(random.random()>0.7): 
            shoot_ball(coordinates,bos,balls)
    else:
        mand.update_score(100)
        bos.remove()
    return coordinates
def won():
    if bos.dead():
        mand.update_score(100)
        update_score(mand)
        print("WELL DONE!")
        exit(1)
while True:
    move(coordinates)
    gravity(coordinates,gra)
    movement(coordinates,zappers,coins,magnets,bullets)
    update_score(mand)
    make_obstacles(coordinates,zappers,coins,magnets)
    collision(coordinates,zappers,coins,magnets,balls)
    shot_bullets(bullets,zappers,coins,magnets,balls)
    countdown(present)
    won()