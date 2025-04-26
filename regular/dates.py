import re


def extract_dates(text):
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    return re.findall(pattern, text)


# Примеры
text = "Сегодня 25-04-2025, а завтра будет 26-04-2025."
dates = extract_dates(text)
print(dates)  # ['25-04-2025', '26-04-2025']
