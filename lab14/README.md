# Лабораторна робота №14: Логічні вирази та умови
## Мета роботи
Ознайомитись з логічними виразами та умовами у пайтон

## Опис завдання
1. Реалізувати різні алгоритми для роботи з логічними операціями та умовними виразами.
2. Створити функції для:
   - Перевірки істинності умов.
   - Перевірки логічної еквівалентності.
   - Виконання операції XOR.
   - Привітання залежно від умови.
   - Обробки вкладених умов.
   - Підрахунку кількості істинних значень у списку.
   - Перевірки парності бітів у числі.
   - Голосування більшості.
   - Перемикання значення.
   - Тернарної перевірки.
   - Валідації умов.
   - Перевірки ланцюгових умов.
   - Фільтрації істинних значень.
   - Мультиплексування на основі умов.
3. Написати тестові приклади для перевірки роботи функцій.

### Опис функцій
1. **Перевірка істинності умов**
   - Функція `check_truth` перевіряє логічну істинність виразу:
     ```python
     def check_truth(a, b, c):
         return (a and b) or c
     ```
     Приклад використання:
     ```python
     print(check_truth(True, False, True))  # Виведе True
     ```

2. **Перевірка логічної еквівалентності**
   - Функція `logical_equivalence` перевіряє логічну еквівалентність двох значень:
     ```python
     def logical_equivalence(a, b):
         return a == b
     ```
     Приклад використання:
     ```python
     print(logical_equivalence(True, True))  # Виведе True
     print(logical_equivalence(True, False))  # Виведе False
     ```

3. **Виконання операції XOR**
   - Функція `xor` виконує логічну операцію XOR між двома значеннями:
     ```python
     def xor(a, b):
         return (a and not b) or (not a and b)
     ```
     Приклад використання:
     ```python
     print(xor(True, False))  # Виведе True
     print(xor(True, True))  # Виведе False
     ```

4. **Привітання залежно від умови**
   - Функція `greet` повертає привітання або прощання залежно від умови:
     ```python
     def greet(is_hello):
         return "Hello, World!" if is_hello else "Goodbye, World!"
     ```
     Приклад використання:
     ```python
     print(greet(True))  # Виведе "Hello, World!"
     print(greet(False))  # Виведе "Goodbye, World!"
     ```

5. **Обробка вкладених умов**
   - Функція `nested_condition` обробляє вкладені умови:
     ```python
     def nested_condition(x, y, z):
         if x == y == z:
             return "All same"
         elif x != y and y != z and x != z:
             return "All different"
         else:
             return "Neither"
     ```
     Приклад використання:
     ```python
     print(nested_condition(3, 3, 3))  # Виведе "All same"
     print(nested_condition(3, 4, 5))  # Виведе "All different"
     ```

6. **Підрахунок кількості істинних значень у списку**
   - Функція `count_true` підраховує кількість істинних значень у списку:
     ```python
     def count_true(bool_list):
         return bool_list.count(True)
     ```
     Приклад використання:
     ```python
     print(count_true([True, False, True, False, True]))  # Виведе 3
     ```

7. **Перевірка парності бітів у числі**
   - Функція `parity` перевіряє парність кількості одиничних бітів у числі:
     ```python
     def parity(n):
         return bin(n).count('1') % 2 == 0
     ```
     Приклад використання:
     ```python
     print(parity(3))  # Виведе False
     ```

8. **Голосування більшості**
   - Функція `majority_vote` визначає, чи більшість з трьох значень є істинною:
     ```python
     def majority_vote(a, b, c):
         return (a + b + c) > 1
     ```
     Приклад використання:
     ```python
     print(majority_vote(True, True, False))  # Виведе True
     ```

9. **Перемикання значення**
   - Функція `switch` перемикає логічне значення на протилежне:
     ```python
     def switch(value):
         return not value
     ```
     Приклад використання:
     ```python
     print(switch(True))  # Виведе False
     ```

10. **Тернарна перевірка**
    - Функція `ternary_check` виконує тернарну операцію перевірки:
      ```python
      def ternary_check(condition, true_result, false_result):
          return true_result if condition else false_result
      ```
      Приклад використання:
      ```python
      print(ternary_check(True, "Yes", "No"))  # Виведе "Yes"
      ```

11. **Валідація умов**
    - Функція `validate` перевіряє виконання логічної умови:
      ```python
      def validate(x, y, z):
          return x or (y and z)
      ```
      Приклад використання:
      ```python
      print(validate(True, False, True))  # Виведе True
      ```

12. **Перевірка ланцюгових умов**
    - Функція `chain_check` перевіряє ланцюгові умови на збільшення або зменшення:
      ```python
      def chain_check(a, b, c):
          if a < b < c:
              return "Increasing"
          elif a > b > c:
              return "Decreasing"
          else:
              return "Neither"
      ```
      Приклад використання:
      ```python
      print(chain_check(1, 2, 3))  # Виведе "Increasing"
      print(chain_check(3, 2, 1))  # Виведе "Decreasing"
      ```

13. **Фільтрація істинних значень**
    - Функція `filter_true` фільтрує істинні значення з списку:
      ```python
      def filter_true(bool_list):
          return [b for b in bool_list if b]
      ```
      Приклад використання:
      ```python
      print(filter_true([True, False, True, False]))  # Виведе [True, True]
      ```

14. **Мультиплексування на основі умов**
    - Функція `multiplexer` повертає значення на основі умов:
      ```python
      def multiplexer(a, b, c, n):
          if a:
              return n * 2
          elif b:
              return n * 3
          elif c:
              return n - 5
          else:
              return n
      ```
      Приклад використання:
      ```python
      print(multiplexer(False, False, True, 10))  # Виведе 5
      ```

## Висновок

В ході лабораторної роботи були реалізовані та протестовані різні алгоритми для роботи з логічними операціями та умовними виразами. Отримані результати підтвердили правильність роботи алгоритмів. Функції показали свою ефективність у вирішенні різних задач, таких як перевірка істинності умов, обробка вкладених умов, голосування більшості та інші. Ця робота допомогла закріпити знання з основних логічних операцій та умовних виразів у Python.

### Інструкції з запуску
1. Встановіть Python версії 3.12.
2. Запустіть скрипт.
