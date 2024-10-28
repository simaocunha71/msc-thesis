"""
import re

def find_literals(text, pattern):
    regex = re.compile(pattern)
    match = regex.search(text)
    if match:
        return match.group(), match.start(), match.end()
    return None, None, None
"""
