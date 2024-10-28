import re
def find_literals(text, pattern):
    matches = re.finditer(pattern, text)
    for match in matches:
        return (match.group(), match.start(), match.end())