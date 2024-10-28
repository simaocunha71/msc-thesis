import re

def find_literals(string, regex):
    pattern = re.compile(regex)
    match = pattern.search(string)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None, None, None
