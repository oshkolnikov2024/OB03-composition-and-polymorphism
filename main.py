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


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} был добавлен в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} был добавлен в персонал.")

    def list_animals(self):
        print("Животные зоопарка:")
        for animal in self.animals:
            print(f"- {animal.name}, Возраст: {animal.age}")

    def list_staff(self):
        print("Персонал зоопарка:")
        for staff in self.staff:
            print(f"- {staff.name}, должность: {staff.position}")


# Создание класса для Сотрудников для использования в композиции
class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

zoo = Zoo()

# Пример использования
bird = Bird("Соловей", 2, 5)
mammal = Mammal("Лев", 4, "золотой")
reptile = Reptile("Змея", 1, "склизкая")

zoo.add_animal(Bird("Соловей", 2, 5))
zoo.add_animal(Mammal("Лев", 4, "золотой"))
zoo.add_animal(Reptile("Змея", 1, "склизкая"))

zoo.add_staff(Staff("Вася Пупкин", "сторож"))
zoo.add_staff(Staff("Света Пуговкина", "Директор"))

animals = [bird, mammal, reptile]

zoo.list_animals()
animal_sound(animals)
zoo.list_staff()