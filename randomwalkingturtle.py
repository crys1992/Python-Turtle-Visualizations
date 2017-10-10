from turtle import *
from random import *
from colorsys import *
 
lengthOfStep=5                 
numberOfSteps=10000
halfSteps = numberOfSteps/5      
hueIncrement=1.0/halfSteps   
width(2)              
 
(w,h)=screensize()     
speed('fastest')
colormode(1.0)          
bgcolor('black')       
angle = 175
hue=0.0
for i in range(numberOfSteps):
    setheading(randint(-369,369))
    color(hsv_to_rgb(hue, 1.0, 1.0)) 
    hue+=hueIncrement                         
    forward(lengthOfStep)                       
    (x,y)=pos()       
    if abs(x)>w or abs(y)>h:            
        backward(lengthOfStep)  

done()
