# Imports go at the top
from microbit import *
import random

def countdown():
    for i in range(3,0,-1):
        display.show(i)
        sleep(1000)
        

def action(speed, type):
    gameover = True
    display.show(type)
    time=0 
    direction = compass.heading()
    maxHeading = direction + 90
    minHeading = direction - 90
    while time < speed :
        newHeading = compass.heading() > direction + 90
        if type == "B" and gameover:
            if accelerometer.was_gesture('3g') :
               gameover = False
            elif button_a.was_pressed() or newHeading:
                return gameover
        if type == "P" and gameover:
            if button_a.was_pressed(): 
                gameover = False
            elif accelerometer.was_gesture('3g') or newHeading:
                return gameover
        if type == "T" and gameover:
            if newHeading:
                gameover = False
            elif button_a.was_pressed() or accelerometer.was_gesture('3g'):
                return gameover
        sleep(1)
        time+=1
    display.clear()
    return gameover

def randChoice():
    g=0
    choice = random.randrange(0,2)
    if choice == 0:
        g=action(speed,"B")
    elif choice == 1:
        g=action(speed,"P")
    elif choice == 2:
        g=action(speed,"T")
    return g    

# Code in a 'while True:' loop repeats forever
while True:
    speed=300
    score=-1
    gameover = False
    countdown()
    while (not gameover):
        score+=1
        gameover=randChoice()
        sleep(200)
    display.scroll("Score "+ str(score))
    display.scroll("Again?")
    
   
