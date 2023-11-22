class person:
    def __init__(self, name, age=0, weight=0): # this is the initialiser. defaults are done by age=0 and weight=0
        self.name = name # attributes here 
        self.age = age
        self.weight = weight

    def display(self): # method (function in oop)
        print(f"{self.name} is {self.age} years old and weighs {self.weight}kg")

class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A static method
  @staticmethod
  def the_laws():
    print(Robot.laws)

  # a class method
  @classmethod
  def assemble(cls):
    return cls("Assembled Robot")

  # An initialiser (special instance method)
  def __init__(self, name = "Robot"):

    # An instance attribute
    self.name = name
    self.age = 0

  # An instance method
  def display(self):
    print(f"I am {self.name}")

if __name__ == "__main__":
    jane = person("Jane Smith", 26, 65)
    robo = Robot("hehe")

    jane.display()
    robo.display()