import re

def clean_data(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))

def filter_emails(emails):
    return list(filter(lambda email: email.count('@') == 1, re.split(r'\s+', emails)))

def extract_keywords(words, length):
    return list(filter(lambda word: len(word) > length, words.split()))

def process_text(text):
    processed = map(lambda x: re.sub(r'\W+', '', x.strip().lower()), text.split(','))
    return list(filter(lambda x: len(x) > 0, processed))

def normalize_data(numbers):
    nums = list(map(float, numbers.split(',')))
    max_num = max(nums)
    return list(map(lambda x: round(x / max_num, 3), nums))

def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

def sum_numeric_strings(numbers):
    return sum(map(int, filter(lambda x: x.isdigit(), numbers.split(','))))

def filter_numbers(numbers, threshold):
    return list(filter(lambda x: int(x) > threshold, filter(lambda x: x.isdigit(), numbers.split())))

def map_to_squares(numbers):
    return list(map(lambda x: int(x)**2, filter(lambda x: x.isdigit(), numbers.split(','))))

def reverse_strings(words):
    return list(map(lambda word: word[::-1], words.split(',')))

if __name__ == "__main__":
    data = "   Apple, Banana , orange "
    cleaned = clean_data(data)
    print(cleaned)  # ['apple', 'banana', 'orange']

    emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
    valid_emails = filter_emails(emails)
    print(valid_emails)  # ['test@example.com', 'example@test.co']

    words = "apple pear banana kiwi"
    filtered_words = extract_keywords(words, 4)
    print(filtered_words)  # ['apple', 'banana']

    texts = "  Hello!  , Yes? , No. ,   "
    processed_texts = process_text(texts)
    print(processed_texts)  # ['hello', 'yes', 'no']

    numbers = "10, 20,30"
    normalized_numbers = normalize_data(numbers)
    print(normalized_numbers)  # [0.333, 0.667, 1.0]

    data = "hello*world*again"
    concatenated = concatenate_strings(data, '*')
    print(concatenated)  # 'helloworldagain'

    numbers = "1, 2, test,  3, 4"
    total_sum = sum_numeric_strings(numbers)
    print(total_sum)  # 10

    numbers = "10 test30 40"
    filtered = filter_numbers(numbers, 25)
    print(filtered)  # [30, 40]

    numbers = "1, 2, 3, 4"
    squared_numbers = map_to_squares(numbers)
    print(squared_numbers)  # [1, 4, 9, 16]

    words = "apple,banana,carrot"
    reversed_words = reverse_strings(words)
    print(reversed_words)  # ['elppa', 'ananab', 'torrac']
