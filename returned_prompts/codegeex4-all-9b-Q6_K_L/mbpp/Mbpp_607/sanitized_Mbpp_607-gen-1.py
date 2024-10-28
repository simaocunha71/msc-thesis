import re
def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return match.group(0), match.start(), match.end()
    else:
        return None