import re
def find_literals(string, literal):
    pattern = re.compile(literal)
    match = pattern.search(string)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None, None, None