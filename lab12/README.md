# Лабораторна робота №12: Робота з матрицями у Python

## Мета роботи
Ознайомтеся з обробкою матриць у Python. Навчіться реалізовувати базові операції з матрицями, такі як додавання, перестановка та множення елементів, перевірка на симетрію, обертання, перетворення в одновимірний масив та отримання діагоналей.

## Опис завдання
1. реалізувати клас `Matrix` для роботи з матрицями.
2. створити наступні методи:
   - Додати елементи до матриці.
   - Обчислити суму елементів рядка.
   - Транспонувати матрицю.
   - Помножити матрицю.
   - Перевірка симетрії матриці.
   - Повернути матрицю на 90° праворуч.
   - Перетворити матрицю в одновимірний масив.
   - Знайти діагональ матриці.
3. написати тестові кейси для перевірки роботи методів.


### Опис класу та методів
1. **Клас `Matrix`**
   - Ініціалізація матриці з заданими кількістю рядків та стовпців:
     ```python
     class Matrix:
         def __init__(self, rows, cols):
             self.rows = rows
             self.cols = cols
             self.data = [[0 for _ in range(cols)] for _ in range(rows)]
     ```
     Приклад використання:
     ```python
     matrix = Matrix(2, 3)
     print(matrix.data)  # Виведе [[0, 0, 0], [0, 0, 0]]
     ```

2. **Додавання елементів до матриці**
   - Метод `add_element` додає елемент до заданої позиції:
     ```python
     def add_element(self, row, col, value):
         if 0 <= row < self.rows and 0 <= col < self.cols:
             self.data[row][col] = value
         else:
             raise IndexError("Індекс поза діапазоном")
     ```
     Приклад використання:
     ```python
     matrix.add_element(1, 2, 10)
     print(matrix.data)  # Виведе [[0, 0, 0], [0, 0, 10]]
     ```

3. **Обчислення суми елементів у рядках**
   - Метод `sum_of_rows` повертає список сум елементів кожного рядка:
     ```python
     def sum_of_rows(self):
         return [sum(row) for row in self.data]
     ```
     Приклад використання:
     ```python
     matrix.add_element(0, 0, 5)
     matrix.add_element(0, 1, 10)
     print(matrix.sum_of_rows())  # Виведе [15, 10]
     ```

4. **Транспонування матриці**
   - Метод `transpose` повертає транспоновану матрицю:
     ```python
     def transpose(self):
         transposed_data = [[self.data[row][col] for row in range(self.rows)] for col in range(self.cols)]
         return Matrix.from_list(transposed_data)
     ```
     Приклад використання:
     ```python
     transposed = matrix.transpose()
     print(transposed.data)  # Виведе [[5, 0], [10, 0], [0, 10]]
     ```

5. **Множення матриць**
   - Метод `multiply_by` множить поточну матрицю на іншу:
     ```python
     def multiply_by(self, other):
         if self.cols != other.rows:
             raise ValueError("Несумісні матриці для множення")

         result = Matrix(self.rows, other.cols)
         for i in range(self.rows):
             for j in range(other.cols):
                 result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
         return result
     ```
     Приклад використання:
     ```python
     matrix1 = Matrix(2, 3)
     matrix1.add_element(0, 0, 1)
     matrix1.add_element(0, 1, 2)
     matrix1.add_element(0, 2, 3)

     matrix2 = Matrix(3, 2)
     matrix2.add_element(0, 0, 1)
     matrix2.add_element(1, 0, 2)
     matrix2.add_element(2, 0, 3)

     result = matrix1.multiply_by(matrix2)
     print(result.data)  # Виведе [[14, 0], [0, 0]]
     ```

6. **Перевірка симетричності матриці**
   - Метод `is_symmetric` перевіряє, чи є матриця симетричною:
     ```python
     def is_symmetric(self):
         if self.rows != self.cols:
             return False

         for i in range(self.rows):
             for j in range(self.cols):
                 if self.data[i][j] != self.data[j][i]:
                     return False
         return True
     ```
     Приклад використання:
     ```python
     matrix = Matrix(2, 2)
     matrix.add_element(0, 1, 5)
     matrix.add_element(1, 0, 5)
     print(matrix.is_symmetric())  # Виведе True
     ```

7. **Обертання матриці на 90 градусів вправо**
   - Метод `rotate_right` обертає матрицю:
     ```python
     def rotate_right(self):
         rotated_data = [[self.data[self.rows - 1 - col][row] for col in range(self.rows)] for row in range(self.cols)]
         self.data = rotated_data
         self.rows, self.cols = self.cols, self.rows
     ```
     Приклад використання:
     ```python
     matrix.add_element(0, 0, 1)
     matrix.add_element(0, 1, 2)
     matrix.add_element(1, 0, 3)
     matrix.add_element(1, 1, 4)
     matrix.rotate_right()
     print(matrix.data)  # Виведе [[3, 1], [4, 2]]
     ```

8. **Перетворення матриці в одновимірний масив**
   - Метод `flatten` повертає одновимірний масив:
     ```python
     def flatten(self):
         return [element for row in self.data for element in row]
     ```
     Приклад використання:
     ```python
     print(matrix.flatten())  # Виведе [3, 1, 4, 2]
     ```

9. **Отримання діагоналі матриці**
   - Метод `diagonal` повертає діагональ матриці:
     ```python
     def diagonal(self):
         if self.rows != self.cols:
             raise ValueError("Матриця не квадратна")

         return [self.data[i][i] for i in range(self.rows)]
     ```
     Приклад використання:
     ```python
     matrix = Matrix(3, 3)
     matrix.add_element(0, 0, 1)
     matrix.add_element(1, 1, 2)
     matrix.add_element(2, 2, 3)
     print(matrix.diagonal())  # Виведе [1, 2, 3]
     ```

10. **Створення матриці з списку списків**
    - Статичний метод `from_list` створює матрицю з списку списків:
      ```python
      @staticmethod
      def from_list(list_of_lists):
          rows = len(list_of_lists)
          cols = len(list_of_lists[0]) if rows > 0 else 0
          matrix = Matrix(rows, cols)
          matrix.data = list_of_lists
          return matrix
      ```
      Приклад використання:
      ```python
      list_of_lists = [[1, 2], [3, 4]]
      matrix = Matrix.from_list(list_of_lists)
      print(matrix.data)  # Виведе [[1, 2], [3, 4]]
      ```

## Результати
Виконання методів класу Matrix продемонструвало їх коректність та ефективність при розв'язанні відповідних задач, пов'язаних з матрицями.

## Висновки
Успішно реалізував та протестував різні методи роботи з матрицями. Під час роботи я зіткнувся з деякими труднощами з реалізацією обертання та множення матриць, але всі вони були успішно вирішені.

## Інструкції з запуску
1. Встановіть Python версії 3.12
2. Запустити код

