# Header comments here 
# FILL THIS OUT!
# Name
# Date
# Project
# Class

from random import *

    # Project time, I'm going to show you how to orgnaize and make one, a simple one.
    # The project I'm going to start is a simple game program. 
def main():
    randNum = randint(0, 100)

    textInput = True
    numInput = -1
    guess = 0
    while(numInput != randNum):
        textInput = input("What's your guess? ")
        numInput = int(textInput)
        guess += 1
        if(randNum < numInput):
            print("Lower")
        elif(randNum > numInput):
            print("Higher")
        else:
            break # Breaks the current loop completely.
    print(f"It took you {guess} guesses to win!")
        
        


# Checks if the name of the file is the main file and then runs it if true
if __name__ == "__main__":
    main()