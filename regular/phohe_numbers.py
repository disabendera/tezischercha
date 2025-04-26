import re


def extract_phone_numbers(text):
    pattern = r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}'
    return re.findall(pattern, text)


# Примеры
text = "Мой телефон +7(123)456-78-90, а у друга +7(987)654-32-10."
numbers = extract_phone_numbers(text)
print(numbers)  # ['+7(123)456-78-90', '+7(987)654-32-10']
