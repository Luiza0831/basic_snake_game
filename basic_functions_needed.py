import os,time,keyboard
import numpy as np

def print_map(map):
    os.system('cls')
    for row in map:
        print("".join(row))

def keyboard_input():
    if keyboard.is_pressed('w'):
        return "up"
    if keyboard.is_pressed('a'):
        return "left"
    if keyboard.is_pressed('s'):
        return "down"
    if keyboard.is_pressed('d'):
        return "right"

m="\033[40;37m \033[m"
s="\033[40;37mx\033[m"
map=np.full((15,35),m)
map[7][17]=s
x=7
y=17

def go_up():
    global x,y,map,m,s
    x-=1
    if x<0:
        x=14
    map=np.full((15,35),m)
    map[x][y]=s

def go_left():
    global x,y,map,m,s
    y-=1
    if y<0:
        y=34
    map=np.full((15,35),m)
    map[x][y]=s

def go_down():
    global x,y,map,m,s
    x+=1
    if x>14:
        x=0
    map=np.full((15,35),m)
    map[x][y]=s

def go_right():
    global x,y,map,m,s
    y+=1
    if y>34:
        y=0
    map=np.full((15,35),m)
    map[x][y]=s