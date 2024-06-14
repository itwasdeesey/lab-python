import re
from itertools import groupby
from statistics import mean, stdev

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

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def process_batches(lst, batch_size):
    return [max(lst[i:i + batch_size]) for i in range(0, len(lst), batch_size)]

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

def rotate_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]) - 1, -1, -1)]

def regex_search(strings, pattern):
    regex = re.compile(pattern)
    return [string for string in strings if regex.search(string)]

def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

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

def group_by_key(items, key):
    grouped = {}
    for item in items:
        grouped.setdefault(item[key], []).append(item['value'])
    return grouped

def remove_outliers(lst):
    if len(lst) < 2:
        return lst
    m = mean(lst)
    s = stdev(lst)
    return [x for x in lst if abs(x - m) <= 2 * s]

print(interpolate_missing([1, None, None, 4]))  #[1, 2, 3, 4]

for num in fibonacci(5):
    print(num)  #0, 1, 1, 2, 3

print(process_batches([1, 2, 3, 4, 5, 6], 2))  #[2, 4, 6]

encoded = encode_string("aaabbc")
print(encoded)  # "3a2bc"
print(decode_string(encoded))  # "aaabbc"

matrix = [
    [1, 2],
    [3, 4]
]
print(rotate_matrix(matrix))  #  [[3, 1], [4, 2]]

print(regex_search(["test", "test123", "none"], "test\\d+"))  #["test123"]

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]

print(is_prime(11))  # True

data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
print(group_by_key(data, 'key'))  # {'a': [1, 3], 'b': [2]}

print(remove_outliers([10, 100, 200, 300, 400, 500, 600]))  #  [100, 200, 300, 400, 500]
