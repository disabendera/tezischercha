import re


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# Примеры
print(is_valid_email("example@example.com"))  # True
print(is_valid_email("invalid-email"))        # False
