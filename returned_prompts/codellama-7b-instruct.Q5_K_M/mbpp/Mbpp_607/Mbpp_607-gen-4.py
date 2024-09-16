import re

def find_literals(pattern, search_string):
    pattern = re.compile(pattern)
    match = pattern.search(search_string)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None


