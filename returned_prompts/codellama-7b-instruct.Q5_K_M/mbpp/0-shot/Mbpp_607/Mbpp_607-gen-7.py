"""
import re

def find_literals(input_string, pattern):
    match = re.search(pattern, input_string)
    if match:
        return match.group(0), match.start(), match.end()
    return None, None, None
"""
