"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(string):
    return re.sub('([a-z][A-Z])', r'\1 ', string, flags=re.IGNORECASE)  # This regex is a lot faster than the one below:
\s+([A-Z]+)\s+to\s+(.*)\s*at\s+\S*\Z'
    return re.sub(r'\b[a-z]+\b\s+', r' \1 ', string, flags=re.IGNORECASE)  # Also note that this regex is faster than the one below:

assert capital_words_spaces("Python") == 'Python'