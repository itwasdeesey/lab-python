# **Лабораторна робота №8**

## 1. Мета роботи
Мета цієї лабораторної роботи — ознайомитися з обробкою файлів JSON у Python і навчитися завантажувати, змінювати та перевіряти дані у форматі JSON.

## 2. Опис завдання
У даній лабораторній роботі ми вирішимо такі завдання:
1. Прочитайте імена людей, вік яких перевищує заданий поріг.
2. Записати дані у файл JSON.
3. Переконайтеся, що файл JSON відповідає вказаній схемі.
4. Пошук значення за ключем у вкладеній структурі JSON.
5. Оновіть значення в об’єкті JSON на основі категорії.

## 3. Виконання роботи
### Структура проекту
- `main.py`: Основний код програми, який містить всі функції завдань.
- `README.md`: Файл з детальним поясненням виконаної роботи.

### Опис кожного файлу та його призначення
- `main.py`: містить реалізацію всіх завдань, таких як зчитування, запис, валідація, пошук та оновлення даних у JSON файлах.

### Опис основних функцій та методів з поясненням їх роботи
```python

import json

def task1(file_path, age_threshold):       #Повертає список імен людей, вік яких перевищує заданий поріг.
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above_age_threshold = [person['name'] for person in data if person['age'] > age_threshold]
    return names_above_age_threshold

def task2(data, file_path):  #Записує дані у файл JSON.
    with open(file_path, 'w') as file:
        json.dump(data, file)

def task3(schema, file_paths):   #Перевіряє файли JSON на відповідність заданій схемі та повертає список невалідних файлів.
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
        try:
            jsonschema.validate(data, schema)
        except jsonschema.exceptions.ValidationError:
            invalid_files.append(file_path)
    return invalid_files

def task4(file_path, key):      #Повертає список значень за заданим ключем у вкладених структурах JSON.
    def search_nested(obj, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    yield v
                elif isinstance(v, (dict, list)):
                    yield from search_nested(v, key)
        elif isinstance(obj, list):
            for item in obj:
                yield from search_nested(item, key)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return list(search_nested(data, key))

def task5(file_path, category, update_func):     #Оновлює значення у JSON об'єктах на основі категорії, зокрема, функція increase_price збільшує значення ціни на 10.
    with open(file_path, 'r+') as file:
        data = json.load(file)
        for item in data:
            if item['category'] == category:
                update_func(item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def increase_price(item):
    item['price'] += 10    
```

## 4.  Висновок

Мета цієї роботи — навчитися працювати з файлами JSON у Python, зокрема читати, змінювати та перевіряти дані. Усі завдання були успішно виконані.

## 5. Інструкції з запуску

### Вимоги до середовища

    Python 3.6+
    Бібліотеки: json
