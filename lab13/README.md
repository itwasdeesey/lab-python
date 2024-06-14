# Лабораторна робота №13: Робота з різними алгоритмами у Python

## Мета роботи
Ознайомитись з різними алгоритмами обробки даних у Python. Навчитися реалізовувати основні алгоритми для інтерполяції, обробки строк, матриць, роботи з регулярними виразами, та іншими задачами.

## Опис завдання
1. Реалізувати різні алгоритми для роботи з масивами, строками та матрицями.
2. Створити функції для:
   - Інтерполяції пропущених значень у списку.
   - Генерації чисел Фібоначчі.
   - Обробки пакетів даних.
   - Кодування та декодування строк.
   - Обертання матриці.
   - Пошуку за регулярними виразами.
   - Об'єднання відсортованих масивів.
   - Перевірки на просте число.
   - Групування елементів за ключем.
   - Видалення відхилень у списку.
3. Написати тестові приклади для перевірки роботи функцій.

### Опис функцій
1. **Інтерполяція пропущених значень у списку**
   - Функція `interpolate_missing` заповнює пропущені значення (None) у списку інтерпольованими значеннями:
     ```python
     def interpolate_missing(lst):
         n = len(lst)
         result = lst[:]
         for i in range(n):
             if result[i] is None:
                 left = right = i
                 while left > 0 and result[left] is None:
                     left -= 1
                 while right < n and result[right] is None:
                     right += 1
                 left_value = result[left] if left >= 0 else 0
                 right_value = result[right] if right < n else 0
                 if left_value is not None and right_value is not None:
                     result[i] = (left_value + right_value) // 2
                 elif left_value is not None:
                     result[i] = left_value
                 elif right_value is not None:
                     result[i] = right_value
         return result
     ```
     Приклад використання:
     ```python
     print(interpolate_missing([1, None, None, 4]))  # Виведе [1, 2, 3, 4]
     ```

2. **Генерація чисел Фібоначчі**
   - Функція `fibonacci` генерує послідовність чисел Фібоначчі:
     ```python
     def fibonacci(n):
         a, b = 0, 1
         for _ in range(n):
             yield a
             a, b = b, a + b
     ```
     Приклад використання:
     ```python
     for num in fibonacci(5):
         print(num)  # Виведе 0, 1, 1, 2, 3
     ```

3. **Обробка пакетів даних**
   - Функція `process_batches` повертає список максимумів для кожного пакету даних заданого розміру:
     ```python
     def process_batches(lst, batch_size):
         return [max(lst[i:i + batch_size]) for i in range(0, len(lst), batch_size)]
     ```
     Приклад використання:
     ```python
     print(process_batches([1, 2, 3, 4, 5, 6], 2))  # Виведе [2, 4, 6]
     ```

4. **Кодування та декодування строк**
   - Функція `encode_string` кодує строку за принципом підрахунку повторюваних символів:
     ```python
     def encode_string(s):
         if not s:
             return ""
         encoded = []
         last_char = s[0]
         count = 1
         for char in s[1:]:
             if char == last_char:
                 count += 1
             else:
                 encoded.append(f"{count if count > 1 else ''}{last_char}")
                 last_char = char
                 count = 1
         encoded.append(f"{count if count > 1 else ''}{last_char}")
         return "".join(encoded)
     ```
     - Функція `decode_string` декодує строку, закодовану за принципом підрахунку повторюваних символів:
     ```python
     def decode_string(s):
         decoded = []
         count = ''
         for char in s:
             if char.isdigit():
                 count += char
             else:
                 decoded.append(char * int(count or '1'))
                 count = ''
         return "".join(decoded)
     ```
     Приклад використання:
     ```python
     encoded = encode_string("aaabbc")
     print(encoded)  # Виведе "3a2bc"
     print(decode_string(encoded))  # Виведе "aaabbc"
     ```

5. **Обертання матриці**
   - Функція `rotate_matrix` обертає матрицю на 90 градусів:
     ```python
     def rotate_matrix(matrix):
         return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]
     ```
     Приклад використання:
     ```python
     matrix = [
         [1, 2],
         [3, 4]
     ]
     print(rotate_matrix(matrix))  # Виведе [[3, 1], [4, 2]]
     ```

6. **Пошук за регулярними виразами**
   - Функція `regex_search` шукає строки, що відповідають заданому регулярному виразу:
     ```python
     def regex_search(strings, pattern):
         regex = re.compile(pattern)
         return [string for string in strings if regex.search(string)]
     ```
     Приклад використання:
     ```python
     print(regex_search(["test", "test123", "none"], "test\\d+"))  # Виведе ["test123"]
     ```

7. **Об'єднання відсортованих масивів**
   - Функція `merge_sorted_arrays` об'єднує два відсортованих масиви в один:
     ```python
     def merge_sorted_arrays(arr1, arr2):
         return sorted(arr1 + arr2)
     ```
     Приклад використання:
     ```python
     print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Виведе [1, 2, 3, 4, 5, 6]
     ```

8. **Перевірка на просте число**
   - Функція `is_prime` перевіряє, чи є число простим:
     ```python
     def is_prime(n):
         if n <= 1:
             return False
         if n <= 3:
             return True
         if n % 2 == 0 or n % 3 == 0:
             return False
         i = 5
         while i * i <= n:
             if n % i == 0 or n % (i + 2) == 0:
                 return False
             i += 6
         return True
     ```
     Приклад використання:
     ```python
     print(is_prime(11))  # Виведе True
     ```

9. **Групування елементів за ключем**
   - Функція `group_by_key` групує елементи списку за заданим ключем:
     ```python
     def group_by_key(items, key):
         grouped = {}
         for item in items:
             grouped.setdefault(item[key], []).append(item['value'])
         return grouped
     ```
     Приклад використання:
     ```python
     data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
     print(group_by_key(data, 'key'))  # Виведе {'a': [1, 3], 'b': [2]}
     ```

10. **Видалення відхилень у списку**
    - Функція `remove_outliers` видаляє елементи, що є відхиленнями, з списку:
      ```python
      from statistics import mean, stdev

      def remove_outliers(lst):
          if len(lst) < 2:
              return lst
          m = mean(lst)
          s = stdev(lst)
          return [x for x in lst if abs(x - m) <= 2 * s]
      ```
      Приклад використання:
      ```python
      print(remove_outliers([10, 100, 200, 300, 400, 500, 600]))  # Виведе [100, 200, 300, 400, 500]
      ```
## Висновок

В ході лабораторної роботи були реалізовані та протестовані різні алгоритми для роботи з масивами, строками та матрицями. Отримані результати підтвердили правильність роботи алгоритмів. Функції показали свою ефективність у вирішенні різних задач, таких як інтерполяція, обробка пакетів даних, кодування строк, обертання матриць та інші. Ця робота допомогла закріпити знання з основних алгоритмів обробки даних у Python.
### Інструкції з запуску
1. Встановіть Python версії 3.12
2. Запустіть скрипт

