from animal import Animal


class Database:
    def __init__(self):
        self.animals = {}
        self._last_animal_key = 0

    def add_animal(self, animal):
        self._last_animal_key += 1
        self.animals[self._last_animal_key] = animal
        return self._last_animal_key

    def delete_animal(self, animal_key):
        if animal_key in self.animals:
            del self.animals[animal_key]

    def edit_animal(self, animal_key, animal):
        self.animals[animal_key] = animal

    def get_animal(self, animal_key):
        animal = self.animals.get(animal_key)
        if animal is None:
            return None
        animal_ = Animal(animal.species, year=animal.year)
        return animal_

    def get_animals(self):
        animals = []
        for animal_key, animal in self.animals.items():
            animal_ = Animal(animal.species, year=animal.year)
            animals.append((animal_key, animal_))
        return animals

