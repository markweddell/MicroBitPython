# Imports go at the top
from microbit import *
import random
microGo = []
playerGo = []

def playerGoAdd(letter):
    display.scroll(letter)
    playerGo.append(letter)

def microAddLetter():
    randomNum = random.randrange(65,68)
    microGo.append(chr(randomNum))
       
def playSequence():
    for i in range(len(microGo)):
        display.scroll(microGo[i])

def initialiseGame():
    microGo.clear()
    for i in range(3):
        microAddLetter()
    playSequence()
    playerGo.clear()

initialiseGame()

    
# Code in a 'while True:' loop repeats forever
while True:
  
    if button_a.was_pressed():
        playerGoAdd('A')        #If A is pressed, add 'A' to playerGo array
   
    elif button_b.was_pressed():
        playerGoAdd('B')        #If B is pressed, add 'B' to playerGo array
   
    elif button_a.is_pressed() and button_b.is_pressed():
        playerGoAdd('C')        #If A+B is pressed, add 'C' to playerGo array
    
    
    if len(playerGo) == len(microGo):       #If guesses made, run the array check
        guessCorrect = 0
        for i in range(len(playerGo)):
            if microGo[i] == playerGo[i]:
                guessCorrect = guessCorrect + 1
                
        if guessCorrect == len(microGo):    # Correct!
            microAddLetter()                # add letter to Sequence
            playSequence()                  # play sequence
            playerGo.clear()                # clear player array for next level
            
        else:                               # Wrong!
            if len(microGo) > 3:            # display length achieved
                display.scroll("Length achieved: " + str(len(microGo)-1))
            display.scroll("Try again")     # new game message
            initialiseGame()                # start again
            
            