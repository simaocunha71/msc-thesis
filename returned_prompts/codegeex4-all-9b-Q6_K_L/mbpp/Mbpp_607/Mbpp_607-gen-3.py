import re
def find_literals(string: str, pattern: str) -> tuple:
    match = re.search(pattern, string)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None

