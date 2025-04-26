import re


def extract_links(html):
    pattern = r'<a\s+href="([^"]+)">'
    return re.findall(pattern, html)


# Примеры
html = '<a href="http://example.com">Link1</a> <a href="https://example2.com">Link2</a>'
links = extract_links(html)
print(links)  # ['http://example.com', 'https://example2.com']
