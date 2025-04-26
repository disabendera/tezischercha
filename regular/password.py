import re


def is_strong_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])(?=.{8,})'
    return bool(re.match(pattern, password))


# Примеры
print(is_strong_password("Password123!"))  # True
print(is_strong_password("password"))      # False
