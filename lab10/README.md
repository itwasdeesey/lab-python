# Лабораторна робота №14: Робота з класами та об'єктами у Python

## Мета роботи
Ознайомитися з основними концепціями об’єктно-орієнтованого програмування (ООП) на Python. Навчитися створювати класи, ініціалізувати об’єкти, використовувати успадкування та інкапсуляцію.

## Опис завдання
1. Реалізація класів для роботи з різними об’єктами та їх методами.
2. Створіть класи та об'єкти:
   - Знайомство студента.
   - Показати тварин та їхні звуки.
   - Продемонструвати птахів та їхні можливості польоту.
   - Демонстрація принципів пакування.
   — Обчислить периметр прямокутника.
   - Обчислить середнє значення набору чисел.

### Опис класів та методів
1. **Клас Student**
   - Клас `Student` представляє студента з полями `name`, `age` та `grade`:
     ```python
     class Student:
         def __init__(self, name, age, grade):
             self.name = name
             self.age = age
             self.grade = grade

         def display_info(self):
             return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
     ```
     Приклад використання:
     ```python
     student = Student(name="Ivan", age=30, grade="2")
     print(student.display_info())  # Виведе "Name: Ivan, Age: 30, Grade: 2"
     ```

2. **Клас Animal та його нащадок Dog**
   - Клас `Animal` представляє тварину з полями `name` та `sound`:
     ```python
     class Animal:
         def __init__(self, name, sound):
             self.name = name
             self.sound = sound

         def make_sound(self):
             return f"{self.name}: {self.sound}"
     ```
   - Клас `Dog`, що наслідує `Animal`, додає поле `breed`:
     ```python
     class Dog(Animal):
         def __init__(self, name, sound, breed):
             super().__init__(name, sound)
             self.breed = breed
     ```
     Приклад використання:
     ```python
     animal = Animal(name="Lala", sound="Roar")
     dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz")
     print(animal.make_sound())  # Виведе "Lala: Roar"
     print(dog.make_sound())  # Виведе "Lala: Auuuuuuu"
     ```

3. **Клас Bird та його нащадки Sparrow та Penguin**
   - Клас `Bird` представляє птаха з методом `fly`:
     ```python
     class Bird:
         def fly(self):
             return None
     ```
   - Клас `Sparrow`, що наслідує `Bird`, перевизначає метод `fly`:
     ```python
     class Sparrow(Bird):
         def fly(self):
             return "Sparrow flies high"
     ```
   - Клас `Penguin`, що наслідує `Bird`, перевизначає метод `fly`:
     ```python
     class Penguin(Bird):
         def fly(self):
             return "Penguin cannot fly"
     ```
     Приклад використання:
     ```python
     bird = Bird()
     sparrow = Sparrow()
     penguin = Penguin()
     print(bird.fly())  # Виведе None
     print(sparrow.fly())  # Виведе "Sparrow flies high"
     print(penguin.fly())  # Виведе "Penguin cannot fly"
     ```

4. **Клас Encapsulation**
   - Клас `Encapsulation` демонструє принципи інкапсуляції з публічними, приватними та захищеними полями:
     ```python
     class Encapsulation:
         def __init__(self, public, _private, __protected):
             self.public = public
             self._private = _private
             self.__protected = __protected
     ```
     Приклад використання:
     ```python
     obj = Encapsulation(1, 2, 3)
     print(obj.public)  # Виведе 1
     print(obj._private)  # Виведе 2
     print(obj._Encapsulation__protected)  # Виведе 3
     ```

5. **Клас Rectangle**
   - Клас `Rectangle` представляє прямокутник з методами для обчислення його периметру:
     ```python
     class Rectangle:
         def __init__(self, width, height):
             self.width = width
             self.height = height

         def calculate_perimeter(self):
             return 2 * (self.width + self.height)
     ```
     Приклад використання:
     ```python
     rectangle = Rectangle(width=5, height=4)
     print(rectangle.calculate_perimeter())  # Виведе 18
     ```

6. **Клас AverageCalculator**
   - Клас `AverageCalculator` обчислює середнє значення з набору чисел:
     ```python
     class AverageCalculator:
         def __init__(self, numbers):
             self.numbers = numbers

         def calculate_average(self):
             return sum(self.numbers) / len(self.numbers) if self.numbers else 0
     ```
     Приклад використання:
     ```python
     numbers = [5, 10, 15, 20]
     avg_calculator = AverageCalculator(numbers)
     print(avg_calculator.calculate_average())  # Виведе 12.5
     ```

## Результати
В результаті лабораторної роботи було створено кілька класів, які демонструють основні принципи ООП:
- Створено класи, що представляють учнів, тварин, птахів і прямокутники.
- Спадковість демонструється за допомогою класів «Animal» і «dog», «bird» та їх нащадків «sparrow» і «penguin».
- Показує інкапсуляцію за допомогою класу "обгортки", що містить публічні, приватні та захищені поля.
— Реалізовано методи обчислення периметра прямокутника та середнього значення набору чисел.
- Отримані результати підтверджують правильність реалізованих класів і методів.

## Висновок
Під час виконання лабораторних робіт були реалізовані та апробовані класи для роботи з об’єктами, які продемонстрували основні принципи об’єктно-орієнтованого програмування. Отримані результати підтверджують правильність алгоритму та ефективність використання ООП для вирішення різноманітних завдань.

### Інструкції з запуску
1. Встановіть Python версії 3.12.
2. Запустіть скрипт.
