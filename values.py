import numpy as np

m="\033[40;37m \033[m"
s="\033[40;37mx\033[m"
map=np.full((15,35),m)
map[7][17]=s
x=7
y=17