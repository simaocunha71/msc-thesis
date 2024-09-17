def find_literals(s, pattern):
    import re
    m = re.search(pattern, s)
    if m is None:
        return None
    return (m.group(0), m.start(), m.end())