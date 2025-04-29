import turtle
import time 
import random


t=turtle.Turtle()
class love():
    def character(self):
        for _ in range(100):
            t.color('red')
            t.speed(100)
            t.circle(50)
            t.left(30)
            t.forward(50)
        for _ in range(10):
            for _ in range(10):
               t.write('Fulkumari',align="left",font=("courier",23,"bold"))
               t.goto(t.window_width()//2, 10) 
               time.sleep(0.6)
        

#instance of class
obj1=love()
obj1.character()