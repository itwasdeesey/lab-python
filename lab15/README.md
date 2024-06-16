# Лабораторна робота №15: Обробка даних за допомогою функцій в Python

## Мета роботи
Дізнайтеся, як використовувати функції для обробки й аналізу текстових і числових даних за допомогою стандартної бібліотеки Python.

## Опис завдання
1. Реалізація функцій обробки та аналізу даних:
   - Очищення та стандартизація текстових даних.
   - Фільтрувати адреси електронної пошти.
   - Виділіть ключові слова за довжиною.
   - Обробка та нормалізація тексту.
   - Стандартизація числових даних.
   - Конкатенація рядків.
   - Підсумовування числового рядка.
   - Фільтрувати числа за порогом.
   — Зіставте числа на квадрати.
   - Виворот рядків.

### Опис функцій
1. **Функція clean_data**
   - Очищує текстові дані, видаляючи пробіли та перетворюючи текст на нижній регістр:
     ```python
     def clean_data(data):
         return list(map(lambda x: x.strip().lower(), data.split(',')))
     ```
     Приклад використання:
     ```python
     data = "   Apple, Banana , orange "
     cleaned = clean_data(data)
     print(cleaned)  # ['apple', 'banana', 'orange']
     ```

2. **Функція filter_emails**
   - Фільтрує валідні електронні адреси:
     ```python
     def filter_emails(emails):
         return list(filter(lambda email: email.count('@') == 1, re.split(r'\s+', emails)))
     ```
     Приклад використання:
     ```python
     emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
     valid_emails = filter_emails(emails)
     print(valid_emails)  # ['test@example.com', 'example@test.co']
     ```

3. **Функція extract_keywords**
   - Витягує ключові слова, довжина яких більша за заданий параметр:
     ```python
     def extract_keywords(words, length):
         return list(filter(lambda word: len(word) > length, words.split()))
     ```
     Приклад використання:
     ```python
     words = "apple pear banana kiwi"
     filtered_words = extract_keywords(words, 4)
     print(filtered_words)  # ['apple', 'banana']
     ```

4. **Функція process_text**
   - Обробляє текст, видаляючи непотрібні символи та пробіли:
     ```python
     def process_text(text):
         processed = map(lambda x: re.sub(r'\W+', '', x.strip().lower()), text.split(','))
         return list(filter(lambda x: len(x) > 0, processed))
     ```
     Приклад використання:
     ```python
     texts = "  Hello!  , Yes? , No. ,   "
     processed_texts = process_text(texts)
     print(processed_texts)  # ['hello', 'yes', 'no']
     ```

5. **Функція normalize_data**
   - Нормалізує числові дані відносно максимального значення:
     ```python
     def normalize_data(numbers):
         nums = list(map(float, numbers.split(',')))
         max_num = max(nums)
         return list(map(lambda x: round(x / max_num, 3), nums))
     ```
     Приклад використання:
     ```python
     numbers = "10, 20,30"
     normalized_numbers = normalize_data(numbers)
     print(normalized_numbers)  # [0.333, 0.667, 1.0]
     ```

6. **Функція concatenate_strings**
   - Конкатенує рядки, розділені певним символом:
     ```python
     def concatenate_strings(data, separator):
         return ''.join(data.split(separator))
     ```
     Приклад використання:
     ```python
     data = "hello*world*again"
     concatenated = concatenate_strings(data, '*')
     print(concatenated)  # 'helloworldagain'
     ```

7. **Функція sum_numeric_strings**
   - Сумує числові значення з рядка:
     ```python
     def sum_numeric_strings(numbers):
         return sum(map(int, filter(lambda x: x.isdigit(), numbers.split(','))))
     ```
     Приклад використання:
     ```python
     numbers = "1, 2, test,  3, 4"
     total_sum = sum_numeric_strings(numbers)
     print(total_sum)  # 10
     ```

8. **Функція filter_numbers**
   - Фільтрує числа, які більші за заданий поріг:
     ```python
     def filter_numbers(numbers, threshold):
         return list(filter(lambda x: int(x) > threshold, filter(lambda x: x.isdigit(), numbers.split())))
     ```
     Приклад використання:
     ```python
     numbers = "10 test30 40"
     filtered = filter_numbers(numbers, 25)
     print(filtered)  # [30, 40]
     ```

9. **Функція map_to_squares**
   - Перетворює числа у їх квадрати:
     ```python
     def map_to_squares(numbers):
         return list(map(lambda x: int(x)**2, filter(lambda x: x.isdigit(), numbers.split(','))))
     ```
     Приклад використання:
     ```python
     numbers = "1, 2, 3, 4"
     squared_numbers = map_to_squares(numbers)
     print(squared_numbers)  # [1, 4, 9, 16]
     ```

10. **Функція reverse_strings**
    - Реверсує рядки:
      ```python
      def reverse_strings(words):
          return list(map(lambda word: word[::-1], words.split(',')))
      ```
      Приклад використання:
      ```python
      words = "apple,banana,carrot"
      reversed_words = reverse_strings(words)
      print(reversed_words)  # ['elppa', 'ananab', 'torrac']
      ```

## Результати
В результаті лабораторної роботи створено функції обробки та аналізу текстових і числових даних:
— Очищені та нормалізовані текстові дані.
- Фільтруйте адреси електронної пошти та вилучайте ключові слова.
- Текст оброблений і нормалізований.
- Стандартизуйте числові дані та рядки підключення.
- Підсумуйте числову вісь і відфільтруйте числа за порогом.
- Перетворюйте числа в квадрати та перевертайте рядки.
- Отримані результати підтверджують коректну роботу реалізованих функцій.

## Висновок
У лабораторній роботі були реалізовані та протестовані функції обробки та аналізу даних з використанням стандартних бібліотек Python. Отримані результати підтверджують правильність алгоритму та ефективність використання функцій для вирішення різноманітних задач.

### Інструкції з запуску
1. Встановіть Python версії 3.12.
2. Запустіть скрипт.
