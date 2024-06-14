def sum_of_squares(arr):
    return sum(x**2 for x in arr)

print(sum_of_squares([1, 2, 3]))

def filter_and_sum(arr):
    average = sum(arr) / len(arr)
    return sum(x for x in arr if x >= average)

print(filter_and_sum([1, 2, 3, 4, 10]))


from collections import Counter

def sort_by_frequency(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))

print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6]))


def find_missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)

print(find_missing_number([1, 2, 4, 5]))


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

print(longest_consecutive([100, 4, 200, 1, 3, 2]))


def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))


def array_of_products(arr):
    length = len(arr)
    left_products = [1] * length
    right_products = [1] * length

    for i in range(1, length):
        left_products[i] = left_products[i - 1] * arr[i - 1]

    for i in range(length - 2, -1, -1):
        right_products[i] = right_products[i + 1] * arr[i + 1]

    return [left_products[i] * right_products[i] for i in range(length)]

print(array_of_products([1, 2, 3, 4]))


def max_subarray_sum(arr):
    max_current = max_global = arr[0]

    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current

    return max_global

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))


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

print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


import heapq

def k_closest_points(points, k):
    return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)

print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2))
