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
    while(textInput != randNum):
        textInput = input("What's your guess? ")
        if(randNum < textInput):
            print("Higher")
        else:
            print("Lower")
    print("You win!")
        
        


# Checks if the name of the file is the main file and then runs it if true
if __name__ == "__main__":
    main()