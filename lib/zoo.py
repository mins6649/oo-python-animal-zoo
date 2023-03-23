from lib.animal import Animal

class Zoo:

    all =[]

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    def get_lcoation(self):
        return self.location
    def get_name(self):
        return self.name
    
    # returns a list of all the animal objects!
    def get_animals(self):
        return [ani for ani in Animal.all if ani.zoo == self]
    
    def get_animal_species(self):
        return set([ani.species for ani in self.get_animals()])
    
    def find_by_species(self, species):
        return [ani for ani in self.get_animals() if ani.species == species]
    
    def get_animal_nicknames(self):
        return [ani.nickname for ani in self.get_animals()]
    
    @classmethod
    def find_by_location(cls, location):
        return [zoo for zoo in cls.all if zoo.location == location]
