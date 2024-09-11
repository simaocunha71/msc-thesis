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

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', 'brown') == ('brown', 8, 14)

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', 'dog') is None

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox1') is None

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', '') == (None, None, None)

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', '.*') == ('The quick brown fox jumps over the lazy dog.', 0, 31)

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', '.*') == ('The quick brown fox jumps over the lazy dog.', 0, 31)

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', '.*') == ('The quick brown fox jumps over the lazy dog.', 0, 31)

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', '.*') == ('The quick brown fox jumps over the lazy dog.', 0, 31)

# Run tests
assert find_literals('The quick brown fox jumps over the lazy dog.', '.*') == ('The quick brown fox jumps over the lazy dog.', 0, 31)

# Run tests
assert find_literals('The quick brown fox jumps