def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    return None

print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))

"""
The function `find_literals` uses the `re.search` function to find the pattern in the text. If a match is found, the function returns the matched string, the start index and the end index of the match. If no match is found, the function returns `None`.
"""

assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
assert find_literals('The quick brown fox jumps over the lazy dog.', 'cat') == None

# Exercise 2:

