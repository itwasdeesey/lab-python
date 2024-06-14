import json


def task1(file_path, age_threshold):
    with open(file_path, 'r') as file:
        data = json.load(file)

    names_above_age_threshold = [person['name'] for person in data if person['age'] > age_threshold]
    return names_above_age_threshold


def task2(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
        try:
            jsonschema.validate(data, schema)
        except jsonschema.exceptions.ValidationError:
            invalid_files.append(file_path)
    return invalid_files


def task4(file_path, key):
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


def task5(file_path, category, update_func):
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
