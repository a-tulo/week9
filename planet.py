class Planet:

    def __init__(self, humans = [], robots = [], name = ""):
        self.humans = humans
        self.robots = robots
        self.name = name

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        self.robots.remove(robot)

    def __repr__(self):
        return f'Humans: {self.humans} \n Robots: {self.robots}'
    
    def __str__(self):
        return f'List of humans are {self.humans}, and the list of robots are {self.robots}'
    
if __name__ == "__main__":
    planet = Planet()
    planet.add_human("alex")
    print(repr(planet))
    planet.add_robot("roboMan6000")
    print(repr(planet))