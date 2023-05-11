# Header comments here 
# FILL THIS OUT!
# Name
# Date
# Project
# Class



   # code goes here

def main():
    # Outputs to console
    print("Hello World!")

    # Assigning a variable 
    x = 5
    y = 2

    # Python can do basic math!
    print(x + y)

    # Inputs as well
    stringInput = input("Input To Be Printed: ")

    # String concatnation
    print('=' * 30)

    # Input can be printed out
    print(stringInput)

    # Some basic data need-to-knows
    tup = (1, 2) # Tuple -- holds exactly two values
    dictionary = dict()  # Dictionary -- holds a key and a value ("name", "john")
    array = [1, 2, 3, 4, 5] # Array -- holds many values

    # Many different data types exist, here are the main ones. Python does not need to specify, other languages do

    # int -> Stands for integer (typically 16). Non-decimal value
    # double, long, float -> Holds more data than int, including decimal values
    # string -> Object which holds text
    # object -> Anything you define. Holds whatever you want. Works similar to def main() but with class 
    #           instead of def and no brackets (usually defined in sepearte files)

    # Need to know for potential jobs
    # OOP -> Object Orientated Programming
    # Four Pillars of OOP -> A.PIE or Abstraction, Polymorphism, Inhertiance, Encapsulation
    # Comments are what these hashtag things are, they are best practice.

    # Practice below
    print("=" * 25)
    # Make it say hello and a name.
    print("")


    print("=" * 25)
    # Same thing, but use a variable this time!
    name = ""
    print("")

    print("=" * 25)
    # Same thing, but now use input:

        #  Modify to use input. Can override old name.
    name = ""
    print("")

    print("=" * 25)

    # Bonus Challenge, do everything we did up there for printing the inputed name in one line.
    # If you need a hint, let me know.

    print()

# Checks if the name of the file is the main file and then runs it if true
if __name__ == "__main__":
    main()