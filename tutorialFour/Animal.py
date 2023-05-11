class Animal():

    # Typically, you want to specify these in the constructor
    name = ""
    species = ""
    color = ""
    age = 0

    # This is a constructor. It specifies what happens the moment an instance of this class is created
    # For now, it will not do anything. As a challenge, add some parameters.
    def __init__(self) -> None:
        pass

    def ageUp(self):
        self.age += 1

    

