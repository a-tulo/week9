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
    
if __name__ == "__main__":
    planet = Planet()
    planet.add_human("alex")
    print(repr(planet))
    planet.add_robot("roboMan6000")
    print(repr(planet))