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

    def __repr__(self):
        return f'human(name={self.name}, age ={self.age})'
    
    def __str__(self):
        return f'Human {self.name} is {self.age} years old'
    
if __name__ == "__main__":
    human = Human()
    human.display()
    
