class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Издает звуки")

    def eat(self):
        print("Животное ест.")


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} поёт!")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит!")


class Reptile(Animal):
    def __init__(self, name, age, scale_pattern):
        super().__init__(name, age)
        self.scale_pattern = scale_pattern

    def make_sound(self):
        print(f"{self.name} шипит!")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Пример использования
bird = Bird("Соловей", 2, 5)
mammal = Mammal("Лев", 4, "golden")
reptile = Reptile("Змея", 1, "diamonds")

animals = [bird, mammal, reptile]
animal_sound(animals)