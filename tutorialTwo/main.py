# Header comments here 
# FILL THIS OUT!
# Name
# Date
# Project
# Class


# A simple function/method (functions are not tied to objects but it is used interchangably none the less)
# You can also overload methods, such as below by just specifying what the argument will be if nothing is passed into it.
def printSomeStuff(stuff="Some Stuff"):
    print(stuff)

# Methods can do many different things. They run a portion of code and can handle almost anything the main method can!
def printInput():
    outputText = input("What should be printed: ")
    print(outputText)

# They can also return particular stuff for variables
def returnSum(a, b):
    return a + b


def main():
    # We are going to define some functions and classes, we call them just like we call print. 
    #   <func name>(<params>)   
    #   print("Parameters")
    
    # Gonna make a line variable
    line = "=" * 25
    printSomeStuff(line)
    printSomeStuff()
    printSomeStuff("Custom Text")
    printSomeStuff(line)
    printInput()
    printSomeStuff(line)
    sum = returnSum(1, 2)
    print(sum)
    # alternatively, we could do 
    print(returnSum(1, 2))
    printSomeStuff(line)
    
    # Practice

    # Make a function and call it below
    
   
    # =================================
    exit()
    




# Checks if the name of the file is the main file and then runs it if true
if __name__ == "__main__":
    main()