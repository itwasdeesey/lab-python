def task1(text):
  pattern = r"^[a-z0-9]+$"
  return bool(re.search(pattern, text))

def task2(text):
  pattern = r"[A-Z]+"
  return bool(re.search(pattern, text))

def task3(text):
  pattern = r"^(?:[0-9]{1-3}\.){3}[0-9]{1-3}$"
  return bool(re.search(pattern, text))

def task4(text):
  pattern = r"^([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
  return bool(re.search(pattern, text))

def task5(text):
  pattern = r"^\d{5}(?:-\d{4})?$"
  return bool(re.search(pattern, text))

def task6(text):
  pattern = r"^[a-z0-9_-]+$"
  return bool(re.search(pattern, text)) and (6 <= len(text) <= 12)

def task7(text):
  pattern = r"^([456][0-9]{15}|[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4})$"
  return bool(re.search(pattern, text))

def task8(text):
  pattern = r"^\d{3}-\d{2}-\d{4}$"
  return bool(re.search(pattern, text))

def task9(text):
  pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&])[A-Za-z0-9@#$%^&*]{8,}$"
  return bool(re.search(pattern, text))

def task10(text):
  pattern = r"^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
  return bool(re.search(pattern, text))
