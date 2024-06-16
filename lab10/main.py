class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student = Student(name="Ivan", age=30, grade="2")


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


student = Student(name="Ivan", age=30, grade="2")
print(student.display_info())  # Name: Ivan, Age: 30, Grade: 2


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed


animal = Animal(name="Lala", sound="Roar")
dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz")
print(animal.make_sound())  # Lala: Roar
print(dog.make_sound())  # Lala: Auuuuuuu


class Bird:
    def fly(self):
        return None


class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"


class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"


bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly())  # None
print(sparrow.fly())  # Sparrow flies high
print(penguin.fly())  # Penguin cannot fly


class Encapsulation:
    def __init__(self, public, _private, __protected):
        self.public = public
        self._private = _private
        self.__protected = __protected


obj = Encapsulation(1, 2, 3)
print(obj.public)  # 1
print(obj._private)  # 2
print(obj._Encapsulation__protected)  # 3



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter())  # 18


class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0


numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average())  # Expected output: 12.5
