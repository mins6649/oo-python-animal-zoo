class Animal:

    all = []

    def __init__(self, species, weight, nickname, zoo):
        self._species = species
        self.weight = weight
        self._nickname = nickname
        self.zoo = zoo
        Animal.all.append(self)

    def get_species(self):
        return self._species
    def set_species(self, species):
        if not self.species:
            self._species = species
        else:
            print("cannot change species")
    
    def get_nickname(self):
        return self._nickname
    def set_nickname(self, nickname):
        if not self.nickname:
            self._nickname = nickname
        else:
            print("cannot change nickname")
    species = property(get_species, set_species)
    nickname = property(get_nickname, set_nickname)

    def get_weight(self):
        return self.weight
    def get_zoo(self):
        return self.zoo 
    
    @classmethod
    def find_by_species(cls, species):
        return [ani for ani in cls.all if ani.species == species]
