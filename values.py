import numpy as np

intro_text="\033[1;37;40mPress or hold 'w''a''s''d' to move up, left, down or right.\nDon't hit the walls and try to get as many apples as you can!\nHold 'e' to exit game.\033[m"
gameover="\033[1;37;40mGame Over!\033[m"
goodbye="\033[1;37;40mGoodbye!\033[m"
score="\033[1;37;40mYour score : "
m="\033[40;37m \033[m"
s="\033[40;37mx\033[m"
o="\033[40;37mo\033[m"
p=0
map=np.full((15,35),m)
x=7
y=17
d=''
speedx=0.23
speedy=0.3
game=True

#color code cheat sheet

# TEXT COLOR	CODE	TEXT STYLE	        CODE	BACKGROUND COLOR	CODE
# Black	        30	    No effect	        0	    Black	            40
# Red	        31	    Bold	            1	    Red	                41
# Green	        32	    Faded   	        2	    Green	            42
# Yellow	    33	    Italic	            3	    Yellow	            43
# Blue	        34	    Underline	        4	    Blue	            44
# Purple	    35		Inverted colors     7       Purple	            45
# Cyan	        36		Inverted text color 8       Cyan	            46
# White	        37		Crossed out         9       White	            47