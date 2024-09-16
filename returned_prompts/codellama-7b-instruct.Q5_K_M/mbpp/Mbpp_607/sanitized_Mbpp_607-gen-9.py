import re
def find_literals(string, pattern):
    """
    Find the first occurrence of `pattern` in `string` and return the matching substring, a start index and an end index.
    """
    match = re.search(pattern, string)
    if match:
        return match.group(), match.start(), match.end()
    return None, -1, -1