class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display(self):
        return f"Name: {self.name} Species: {self.species} Age: {self.age}"

    def sound(self):
        print("some generic sound")

    def eat(self):
        print("eating food")


class Mammal(Animal):
    def __init__(self, name, species, age, colour):
        super().__init__(name, species, age)
        self.colour = colour

    def display(self):
        info = super().display()
        return f"Info : {info}  Colour: {self.colour}"

    def sound(self):
        print("mammal sound")


class Bird(Animal):
    def __init__(self, name, species, age, colour, can_fly):
        super().__init__(name, species, age)
        self.colour = colour
        self.can_fly = can_fly

    def display(self):
        info = super().display()
        if self.can_fly:
            return f"Info : {info} can fly : Yes it can fly"
        else:
            return f"Info : {info} can fly : No it can't fly"

    def sound(self):
        print("tweet tweet...")

    def eat(self):
        print("pecking the seeds")


class Fish(Animal):
    def __init__(self, name, species, age, colour, water_type):
        super().__init__(name, species, age)
        self.colour = colour
        self.water_type = water_type

    def display(self):
        info = super().display()
        return f"Info : {info} Water type: {self.water_type}"

    def sound(self):
        print(".....")

    def eat(self):
        print("eating algae")


class Dog(Mammal):
    def __init__(self, name, species, age, colour, breed):
        super().__init__(name, species, age, colour)
        self.breed = breed

    def display(self):
        info = super().display()
        return f"{info}  Breed: {self.breed}"

    def sound(self):
        print("wooff... wooff...")


class Penguin(Bird):
    def __init__(self, name, species, age, colour):
        super().__init__(name, species, age, colour, can_fly=False)

    def sound(self):
        print("honk...")

    def swim(self):
        print("they can swim")


class LandCreature:
    def habitat(self):
        print("they live on land")


class WaterCreature:
    def habitat(self):
        print("they live in water")


class Amphibian(LandCreature, WaterCreature):
    pass


class Frog(Animal, Amphibian):
    def __init__(self, name, species, age):
        Animal.__init__(self, name, species, age)

    def sound(self):
        print("ribbit")

    def habitation(self):
        Amphibian.habitat(self)
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all(self):
        for i in self.animals:
            print(i.display())
            i.sound()
            print("-" * 76)


zoo = Zoo()


zoo.add_animal(Dog("Rex", "Dog", 3, "brown", "Labrador"))
zoo.add_animal(Penguin("Pingu", "Penguin", 4, "black & white"))
zoo.add_animal(Fish("Nemo", "Clownfish", 1, "orange", "salt"))
zoo.add_animal(Frog("Kermit", "Frog", 2))

zoo.show_all()


print("\nFrog MRO:")
print(Frog.__mro__)
