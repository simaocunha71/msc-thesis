import re
def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return match.group(), match.start(), match.end()
    return None