# Header comments here 
# FILL THIS OUT!
# Name
# Date
# Project
# Class

def main():
    # Congrats! This is the penulitmate tutorial!
    # Aren't you glad this tutorial doesn't LOOP back around. Me too!
    # Unforutnately, looping and conditionals are the topics of this tutorial

    # Conditionals are easy! It's simply just true and false... on steroids
    cond = True
    oppositeCond = not cond
    print("Condition 1 : " + cond)
    print("Condition 1's Opposite: " + oppositeCond)

    # Conditional statements happen if true, and don't if not
    if(cond): # checking if cond is true
        print("cond is true")

    # Else If's
    speech = input() 
    
    if(speech == "Hello There"):
        print("You are Obi-Wan")
    elif(speech == "This is the Way"):
        print("You are Mandolorian.")
    else:
        print("You typed something")

    # Different types of comparions operators (NEED TO KNOW)

        # ==  ->  Equality Check (if both are same, they return true)
        # !=  -> Not Equal Check (if both are same, return false)
        # >, >=   ->   Checks if left value is higher than right. Returns true if so.
        # <, <=   ->   Checks if right value is higher than left. Returns true if so.
        # or  -> OR operator    Checks if either condition around it is true (if so, then returns true)
        # and  -> AND operator   Checks if both conditions around it are true (if so, then returns false)
    brotherAge = 10
    sisterAge = 20
    if(brotherAge != sisterAge):
        print("Not twins")

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