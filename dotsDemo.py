#Liam Collins
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

RADIUS = 10

red = Color(0xFF0000,1)

dot = CircleAsset(RADIUS,LineStyle(1,red),red)

for i in range(15): #putting a row of dots
    for j in range(8):
        Sprite(dot,(10+(RADIUS*2+10)*i,10+(RADIUS*2+10)*j))

App().run()
