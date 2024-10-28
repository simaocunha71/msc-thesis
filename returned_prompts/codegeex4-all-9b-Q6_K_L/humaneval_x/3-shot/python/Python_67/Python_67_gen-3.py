    import re
    apple = int(re.findall(r'\d+', re.findall(r'(\d+) apples', fruit_distribution)[0]))
    orange = int(re.findall(r'\d+', re.findall(r'(\d+) oranges', fruit_distribution)[0]))
    return n - apple - orange

