import re


def extract_numbers(text):
    pattern = r'\b\d+\.\d+\b|\b\d+\b'  # Ищем как целые числа, так и числа с плавающей запятой
    return [float(match) for match in re.findall(pattern, text)]


# Примеры
text = "Цена товара 12.99 рублей, а скидка 5%."
numbers = extract_numbers(text)
print(numbers)  # [12.99, 5.0]

text_with_empty = "Цена товара 12.99 и пустая строка , а скидка 5%."
numbers_with_empty = extract_numbers(text_with_empty)
print(numbers_with_empty)  # [12.99, 5.0]
