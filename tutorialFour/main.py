# Header comments here 
# FILL THIS OUT!
# Name
# Date
# Project
# Class

from Animal import Animal
from Cat import Cat

def main():
    # Last Exercise! After this, you will know python and programming in general! At least enough for a job!
    
    # This last exercise is going to be about classes. If you opened this in a folder, you should be good!
    # Classes are a special way of breaking up the work of a program.
    # Classes also hide unnecessary things they do from other classes.
    
    # Classes are blueprints for objects. Objects are the building blocks of the programs.

    # A class can inherit another class as well, this is called inheritance.
    # If that happens, the inherited class is called the parent while the class inheriting is the child
    # Classes are more powerful, but that should be all you need for now.

    # Let's get to making some classes!
    
    # Look at the top, you should see something that says import! That shows which classes are in this scope and can be used here.
    print("=" * 25)
    # Creating an animal and setting it's properties
    myAnimal = Animal()
    myAnimal.name = "Milo"
    myAnimal.ageUp()

    print(myAnimal.name + " is " + str(myAnimal.age) + " years old")
    print("=" * 25)
    # Now, let's make a cat.
    myCat = Cat()
    myCat.name = "Juniper"
    print(myCat.name + " is " + str(myCat.age) + " years old")
    print("=" * 25)
    myCat.speak()
    print("=" * 25)

# Practice by making your own class and calling it's methods here!


# Checks if the name of the file is the main file and then runs it if true
if __name__ == "__main__":
    main()