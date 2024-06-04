import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def make_sound(self):
        return "чирик, чирик"

class Mammal(Animal):
    def make_sound(self):
        return "ррррр"

class Reptile(Animal):
    def make_sound(self):
        return "шшшш"

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} издает звук {animal.make_sound()}.")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_state(self, filename):
        with open(filename, 'w') as file:
            data = {
                "animals": [(animal.name, animal.age, animal.__class__.__name__) for animal in self.animals],
                "employees": [employee.__class__.__name__ for employee in self.employees]
            }
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_state(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for animal in data["animals"]:
                name, age, type_ = animal
                if type_ == "Bird":
                    self.animals.append(Bird(name, age))
                elif type_ == "Mammal":
                    self.animals.append(Mammal(name, age))
                elif type_ == "Reptile":
                    self.animals.append(Reptile(name, age))

class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Хранитель зоопарка кормит {animal.name}.")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит {animal.name}.")


zoo = Zoo()
zoo.add_animal(Bird("Попугай", 3))
zoo.add_animal(Mammal("Тигр", 5))
zoo.add_animal(Reptile("Питон", 2))

zooKeeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_employee(zooKeeper)
zoo.add_employee(veterinarian)

animal_sound(zoo.animals)
zooKeeper.feed_animal(zoo.animals[0])
veterinarian.heal_animal(zoo.animals[1])


zoo.save_state('zoo_state.json')


new_zoo = Zoo()
new_zoo.load_state('zoo_state.json')
animal_sound(new_zoo.animals)