# Лабораторна робота №11: Обробка та аналіз масивів даних

## Мета роботи
Навчіться обробляти та аналізувати масиви даних у Python. Навчіться розв'язувати задачі з масивами за допомогою стандартних бібліотек та алгоритмів.

## Опис завдання
1. Обчислити суму квадратів елементів масиву.
2. Обчисліть суму елементів масиву, які більші або дорівнюють середньому.
3. Відсортувати масив за частотою елементів.
4. Знайди в ряду пропущене число.
5. Знайти довжину найдовшої неперервної підпослідовності.
6. Повернути масив після кругового зсуву k елементів вправо.
7. Обчислити добуток масиву всіх елементів масиву, крім поточного елемента.
8. Знайти максимальну суму підмасивів.
9. Відображення елементів матриці в спіральному порядку.
10. Знайдіть k точок, найближчих до початку координат.


### Опис функцій
1. `sum_of_squares(arr)`: Обчислює суму квадратів елементів масиву `arr`.
    ```python
    def sum_of_squares(arr):
        return sum(x**2 for x in arr)
    ```
    Приклад використання:
    ```python
    print(sum_of_squares([1, 2, 3]))  # Виведе 14
    ```

2. `filter_and_sum(arr)`: Обчислює суму елементів масиву `arr`, які більші або рівні середньому значенню.
    ```python
    def filter_and_sum(arr):
        average = sum(arr) / len(arr)
        return sum(x for x in arr if x >= average)
    ```
    Приклад використання:
    ```python
    print(filter_and_sum([1, 2, 3, 4, 10]))  # Виведе 14
    ```

3. `sort_by_frequency(arr)`: Відсортовує масив `arr` за частотою елементів.
    ```python
    from collections import Counter

    def sort_by_frequency(arr):
        freq = Counter(arr)
        return sorted(arr, key=lambda x: (-freq[x], x))
    ```
    Приклад використання:
    ```python
    print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6]))  # Виведе [4, 4, 4, 6, 6, 6, 2]
    ```

4. `find_missing_number(arr)`: Знаходить відсутнє число у послідовності `arr`.
    ```python
    def find_missing_number(arr):
        n = len(arr) + 1
        return n * (n + 1) // 2 - sum(arr)
    ```
    Приклад використання:
    ```python
    print(find_missing_number([1, 2, 4, 5]))  # Виведе 3
    ```

5. `longest_consecutive(arr)`: Знаходить довжину найдовшої послідовної підпослідовності у масиві `arr`.
    ```python
    def longest_consecutive(arr):
        num_set = set(arr)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
    ```
    Приклад використання:
    ```python
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Виведе 4
    ```

6. `rotate_array(arr, k)`: Повертає масив `arr` після циклічного зсуву вправо на `k` елементів.
    ```python
    def rotate_array(arr, k):
        k = k % len(arr)
        return arr[-k:] + arr[:-k]
    ```
    Приклад використання:
    ```python
    print(rotate_array([1, 2, 3, 4, 5], 2))  # Виведе [4, 5, 1, 2, 3]
    ```

7. `array_of_products(arr)`: Обчислює масив добутків всіх елементів масиву `arr`, крім поточного.
    ```python
    def array_of_products(arr):
        length = len(arr)
        left_products = [1] * length
        right_products = [1] * length

        for i in range(1, length):
            left_products[i] = left_products[i - 1] * arr[i - 1]

        for i in range(length - 2, -1, -1):
            right_products[i] = right_products[i + 1] * arr[i + 1]

        return [left_products[i] * right_products[i] for i in range(length)]
    ```
    Приклад використання:
    ```python
    print(array_of_products([1, 2, 3, 4]))  # Виведе [24, 12, 8, 6]
    ```

8. `max_subarray_sum(arr)`: Знаходить максимальну суму підмасиву `arr`.
    ```python
    def max_subarray_sum(arr):
        max_current = max_global = arr[0]

        for num in arr[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current

        return max_global
    ```
    Приклад використання:
    ```python
    print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Виведе 6
    ```

9. `spiral_order(matrix)`: Виводить елементи матриці `matrix` у спіральному порядку.
    ```python
    def spiral_order(matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result
    ```
    Приклад використання:
    ```python
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Виведе [1, 2, 3, 6, 9, 8, 7, 4, 5]
    ```

10. `k_closest_points(points, k)`: Знаходить `k` найближчих точок до початку координат з масиву `points`.
    ```python
    import heapq

    def k_closest_points(points, k):
        return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)
    ```
    Приклад використання:
    ```python
    print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2))  # Виведе [(1, 1), (1, 2)]
    ```

## Результати
Результати роботи отриманих функцій показують коректність та ефективність розв'язання відповідних задач на масиві.

## Висновки
Були успішно реалізовані та протестовані різні функції для обробки та аналізу набору даних. Під час роботи виникали певні труднощі з оптимізацією алгоритмів, але всі вони були вирішені.

## Інструкції з запуску
1. Встановіть Python версії 3.12
2. Запустіть код


