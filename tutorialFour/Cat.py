from Animal import Animal

# Typed the class it extends from in the paranthesis (have to import the class). Only one parent except in the case of interfaces. If you want to know more, ask me or google!
class Cat(Animal):

    # each method has a self reference which allows it to access it's own properities. I do that with name below.
    def speak(self):
        print(self.name + ": Meow!")