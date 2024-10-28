
import re
def find_literals(s, pattern):
    match = re.search(pattern, s)
    return match.group(), match.start(), match.end()


