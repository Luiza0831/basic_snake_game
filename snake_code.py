import os,time,keyboard
import numpy as np
from values import *

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

def snake():
    global x,y,map
    d='right'
    print_map(map)
    while True:
        if keyboard_input()=='up':
            d='up'
            go_up()
            time.sleep(0.01)
            print_map(map)
        if keyboard_input()=='left':
            d='left'
            go_left()
            time.sleep(0.01)
            print_map(map)
        if keyboard_input()=='down':
            d='down'
            go_down()
            time.sleep(0.01)
            print_map(map)
        if keyboard_input()=='right':
            d='right'
            go_right()
            time.sleep(0.01)
            print_map(map)
        while d=='up':
            if keyboard_input()=='right' or keyboard_input()=='left'or keyboard_input()=='down':
                d=keyboard_input()
                break
            go_up()
            time.sleep(0.25)
            print_map(map)   
        while d=='left':
            if keyboard_input()=='right' or keyboard_input()=='up'or keyboard_input()=='down':
                d=keyboard_input()
                break
            go_left()
            time.sleep(0.2)
            print_map(map)
        while d=='down':
            if keyboard_input()=='right' or keyboard_input()=='left'or keyboard_input()=='up':
                d=keyboard_input()
                break
            go_down()
            time.sleep(0.25)
            print_map(map)
        while d=='right':
            if keyboard_input()=='left' or keyboard_input()=='up'or keyboard_input()=='down':
                d=keyboard_input()
                break
            go_right()
            time.sleep(0.2)
            print_map(map)
snake()