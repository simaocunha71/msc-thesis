def find_literals(s, pattern):
    """
    Finds a regex pattern in a string and returns the match, start index, and end index
    """
    import re
    match = re.search(pattern, s)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None