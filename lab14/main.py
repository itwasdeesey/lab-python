def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(a, b):
    return a == b

def xor(a, b):
    return (a and not b) or (not a and b)

def greet(is_hello):
    return "Hello, World!" if is_hello else "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"

def count_true(bool_list):
    return bool_list.count(True)

def parity(n):
    return bin(n).count('1') % 2 == 0

def majority_vote(a, b, c):
    return (a + b + c) > 1

def switch(value):
    return not value

def ternary_check(condition, true_result, false_result):
    return true_result if condition else false_result

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(bool_list):
    return [b for b in bool_list if b]

def multiplexer(a, b, c, n):
    if a:
        return n * 2
    elif b:
        return n * 3
    elif c:
        return n - 5
    else:
        return n

print(check_truth(True, False, True))
print(logical_equivalence(True, True))
print(logical_equivalence(True, False))
print(xor(True, False))
print(xor(True, True))
print(greet(True))
print(greet(False))
print(nested_condition(3, 3, 3))
print(nested_condition(3, 4, 5))
print(count_true([True, False, True, False, True]))
print(parity(3))
print(majority_vote(True, True, False))
print(switch(True))
print(ternary_check(True, "Yes", "No"))
print(validate(True, False, True))
print(chain_check(1, 2, 3))
print(chain_check(3, 2, 1))
print(filter_true([True, False, True, False]))
print(multiplexer(False, False, True, 10))
