
import re
def find_literals(s: str, p: str) -> tuple:
    regex = re.compile(p)
    match = regex.search(s)
    if match is None:
        return (None, None, None)
    return (match.group(), match.start(), match.end())


