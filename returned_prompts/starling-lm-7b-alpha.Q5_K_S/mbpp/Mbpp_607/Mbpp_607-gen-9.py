"""
def find_literals(string, pattern):
    import re
    m = re.search(pattern, string)
    if m:
        return (m.group(0), m.start(), m.end())
    else:
        return None
"""

