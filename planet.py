import random as rnd
import matplotlib.pyplot as plt
class Human:

    #Class attributes
    MAX_ENERGY = 100

    #initialiser
    def __init__(self, name = "Human", age = 0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    #method
    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'human(name={self.name}, age ={self.age}, energy ={self.energy})'
    
    def __str__(self):
        return f'Human {self.name} is {self.age} years old and my energy is {self.energy}'
    
    def grow(self):
        self.age += 1

    def eat(self, amount):
        potential_energy = self.energy + amount
        if potential_energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
            return potential_energy - self.energy
        else:
            self.energy = potential_energy
            return 0

    def move(self, distance):
        potential_energy = self.energy - distance
        if potential_energy < 0:
            self.energy = 0
            return self.energy - abs(potential_energy)
        else:
            self.energy = potential_energy
            return 0
        
class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"
  MAX_ENERGY = 100

  # A static method
  @staticmethod
  def the_laws():
    print(Robot.laws)

  # a class method
  @classmethod
  def assemble(cls):
    return cls("Assembled Robot")

  # An initialiser (special instance method)
  def __init__(self, name = "Robot", energy = 0):

    # An instance attribute
    self.name = name
    self.age = 0
    self.energy = energy

  # An instance method
  def display(self):
    print(f"I am {self.name}")

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old.'
  
class Planet:

    def __init__(self, name = ""):
        self.name = name
        self.inhabitants = {
        'humans': [],
        'robots': []
        }

    def add_human(self, human):
        self.inhabitants['humans'].append(human)

    def remove_human(self, human):
        self.inhabitants['humans'].remove(human)

    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)

    def remove_robot(self, robot):
        self.inhabitants['robots'].remove(robot)

    def __repr__(self):
        return f'Humans: {self.inhabitants['humans']} \n Robots: {self.inhabitants['robots']}'
    
    def __str__(self):
        return f'List of humans are {self.inhabitants['humans']}, and the list of robots are {self.inhabitants['robots']}'
    
class Universe:

    def __init__(self):
        self.planets = []

    def generate(self):
        for count in range(rnd.randint(1,10)):
            planet = Planet(f"planet {count}")

            for index in range(rnd.randint(1,10)):
                robot = Robot(f"Robot{index}")
                planet.add_robot(robot)

            for index in range(rnd.randint(1,10)):
                human = Human(f"Human{index}")
                planet.add_human(human)

            self.planets.append(planet)

    def __repr__(self):
       return f"universe(planets={self.planets})"

    def show_populations(self, selection):
        x_values = []
        y_values = []

        for planet in self.planets:
            x_values.append(planet.name)

            if selection == "humans":
                y_values.append(len(planet.inhabitants['humans']))
            else:
                y_values.append(len(planet.inhabitants['robots']))

        plt.bar(x_values,y_values)
        plt.tight_layout()
        plt.show()


    
if __name__ == "__main__":
    universe = Universe()
    universe.generate()
    universe.show_populations("humans")
    universe.show_populations("robots")