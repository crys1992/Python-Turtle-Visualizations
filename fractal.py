from turtle import *

def hilbert2(step, rule, angle, depth):
   if depth > 0:
      a = lambda: hilbert2(step, "a", angle, depth - 1)
      b = lambda: hilbert2(step, "b", angle, depth - 1)
      left = lambda: left(angle)
      right = lambda: right(angle)
      forward = lambda: forward(step)
      if rule == "a":
        left(); b(); forward(); right(); a(); forward(); a(); right(); forward(); b(); left();
      if rule == "b":
        right(); a(); forward(); left(); b(); forward(); b(); left(); forward(); a(); right();
        
#myTurtle = turtle.Turtle()
#myTurtle.speed(0)
hilbert2(5, "a", 90, 5)

done()