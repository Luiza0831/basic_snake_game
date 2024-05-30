import os,time,keyboard,random
import numpy as np
from values import *

def print_map(map):
    global p
    os.system('cls')
    print(intro_text,"\n")
    for row in map:
        print("".join(row))
    print(f"\n{score}{p}\033[m")

def keyboard_input():
    global d
    if keyboard.is_pressed('w'):
        d='up'
        return d
    if keyboard.is_pressed('a'):
        d='left'
        return d
    if keyboard.is_pressed('s'):
        d='down'
        return d
    if keyboard.is_pressed('d'):
        d='right'
        return d
    if keyboard.is_pressed('e'):
        d='exit'
        return d

def random_apple():
    global m,o
    mapo=np.full((15,35),m)
    xo=random.randint(1,13)
    yo=random.randint(1,33)
    mapo[xo][yo]=o
    return mapo

def try_print_new_map():
    global x,y,map,mapo,m,s,o,p
    map=mapo
    try:
        if map[x][y]==o:
            p+=1
            mapo=random_apple()
            map=mapo
        map[x][y]=s
    except IndexError:
        pass

def print_gameover():
    print(gameover)
    exit()

def go_up():
    global x,y,map,mapo,m,s,o,p,game
    map[x][y]=m
    x-=1
    if x<0:
        # x=14
        print_gameover()
    try_print_new_map()
    

def go_left():
    global x,y,map,mapo,m,s,p,game
    map[x][y]=m
    y-=1
    if y<0:
        # y=34
        print_gameover()
    try_print_new_map()

def go_down():
    global x,y,map,mapo,m,s,p,game
    map[x][y]=m
    x+=1
    if x>14:
        # x=0
        print_gameover()
    try_print_new_map()

def go_right():
    global x,y,map,mapo,m,s,p,game
    map[x][y]=m
    y+=1
    if y>34:
        # y=0
        print_gameover()
    try_print_new_map()

def where_to_go(d):
    if d=='up':
        go_up()
    if d=='left':
        go_left()
    if d=='down':
        go_down()
    if d=='right':
        go_right()
