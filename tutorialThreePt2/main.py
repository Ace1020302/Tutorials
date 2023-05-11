# Header comments here 
# FILL THIS OUT!
# Name
# Date
# Project
# Class

def main():
    # Now that we've seen how easy conditionals are, let's use them!

    # Looping is what makes a program run over and over until specified (or until something happens)

    # Three Types:
    
    # foreach loops (repeats for each element)
    # for loops (repeats a certain number of times)
    # while loops (repeat until a condition is met)

    # Let's print the sum of three numbers
    numbers = [1, 8, 9] # should add to 18
    sum = 0
    
    # For each loop
    for num in numbers:
        sum += num

    print(sum)
    print("="* 25)

    sum = 0
    # For loop
    for x in range(0, 10):
        if(x % 2 == 0):
            sum += x

    print(sum)
    print("="* 25)

    x = 5
    while (x < 10):
        print(x)

    # Sum is reset again
    sum = 0
    print("="* 25)

    # Practice! Handle some input. Use comparison and add up every number entered. Change the condition in the while loop to what you need
    #   You will need a few things, try googling them.
    #       Try-Catch statement
    #       Parse string to integer in python
    # Bonus: Break it into a method and just call it!

    inText = ""

    while(False): # Change the condition here
        print("Code here")





# Checks if the name of the file is the main file and then runs it if true
if __name__ == "__main__":
    main()