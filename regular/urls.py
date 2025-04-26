import re


def parse_url(url):
    pattern = r'^(https?)://([a-zA-Z0-9.-]+)(/.*)?$'
    match = re.match(pattern, url)
    if match:
        return match.groups()
    return None


# Примеры
url = "https://example.com/path/to/resource"
result = parse_url(url)
print(result)  # ('https', 'example.com', '/path/to/resource')
