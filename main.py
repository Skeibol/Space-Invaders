class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
import re
import numpy as np
import os
import pygame
from pynput import keyboard
from termcolor import colored
#import re 
#print(re.sub('[\.[\]]', ' ', np.array_str(board)))

def ReturnKey(key):
    return key
def on_press(key):
    global press
    try:
        press = key.char

        return key
    except:
        pass


def on_release(key):
    global press 
    press = None
    return

class Spaceship:
    def __init__(self):
        self.x = 5
        self.y = 5
        self.hp = 100
        self.bullets = []
        global press
    def shoot(self):
        
        self.bullets.append(Bullet(self.x,self.y))
        global press
        press = None

        


    def controller(self,press):
        if(press!=None):
            key = press
            if(key=="f"):
                
                self.shoot()
            
            if(key=="a"):
                board[ship.y,ship.x] = 0
                if self.x>0:
                    self.x-=1
                
            elif(key == "d"):
                board[ship.y,ship.x] = 0
                if self.x<19:
                    self.x+=1
            elif(key=="w"):
                board[ship.y,ship.x] = 0
                if self.y>0:
                    self.y-=1
            elif(key == "s"):
                board[ship.y,ship.x] = 0
                if self.y<13:
                    self.y+=1
        
            board[ship.y,ship.x] = 1
    
            
            key = None
            

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y - 1
        self.active = True
    def update(self):
        if board[self.y,self.x] == 3:
            self.active = False
        if(self.y>0) and self.active:
            self.y -= 1
            board[self.y,self.x] = 8
            board[self.y + 1,self.x] = 0
        elif self.active:
            board[self.y,self.x] = 8
            self.active = False
            board[self.y,self.x] = 0

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.alive = True
        self.hp = 50
    def draw(self):
        if board[self.y,self.x] == 8:
            self.hp -= 10
            if self.hp == 0:
                self.alive = False
                board[self.y,self.x] = 0
        if self.alive:
            board[self.y,self.x] = 3

def FormatBoard(board):
    str = np.array2string(board, precision=0, separator=' ',
                      suppress_small=True)
    #str = str.replace(" ", "")
    
    str = str.replace("", " ", 1)
    str = str.replace("]", "")
    str = str.replace("[", "")
    str = str.replace(r".", '')                  
    str = str.replace(r"1", bcolors.FAIL + r'W' + bcolors.OKCYAN)
    str = str.replace(r"8", bcolors.FAIL + r'X' + bcolors.OKCYAN)
    str = str.replace(r"3", bcolors.OKGREEN + r'X' + bcolors.OKCYAN)

    return str
global press
press = None
bullet = None
board = np.zeros((15,20))
ship = Spaceship()
enemies = []
c = 0
listener = keyboard.Listener(
on_press=on_press,
on_release=on_release)
listener.start()
for i in range(10):
    x = np.random.randint(3,9)
    y = np.random.randint(3,9)
    enemies.append(Enemy(x,y))

while True:
    for i in ship.bullets:
        i.update()
    for i in enemies:
        i.draw()
    ship.controller(press)

    board_formatted = FormatBoard(board)
    print(board_formatted)
    
    pygame.time.wait(30)
    
    clear = lambda: os.system('cls')
    print("\033[F"*21)
    #listener.stop()
    #clear()
    c+=1

