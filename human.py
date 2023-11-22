class Human:

    #Class attributes
    MAX_ENERGY = 100

    #initialiser
    def __init__(self, name = "Human", age = 0, energy = MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    

    #method
    def display(self):
        print(f"I am {self.name}")

if __name__ == "__main__":
    human = Human()
    human.display()
    
