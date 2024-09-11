def find_literals(s, pattern):
    '''
    Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
    '''
    import re
    result = re.search(pattern, s)
    return result.group(), result.start(), result.end()


# Test
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
#assert find_literals('The quick brown fox jumps over the lazy dog.', 'lazy') == ('lazy', 30, 34)

#assert find_literals('The quick brown fox jumps over the lazy dog.', 'foxjumps') == ('foxjumps', 16, 25)

#assert find_literals('The quick brown fox jumps over the lazy dog.', 'lazy') == ('lazy', 30, 34)

#assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)


def find_literals(s, pattern):
    '''
    Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
    '''
    import re
    result = re.search(pattern, s)
    return result.group(), result.start(), result.end()


# Test
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
#assert find_literals('The quick brown fox jumps over the lazy dog.', 'lazy') == ('lazy', 30, 34)

#assert find_literals('The quick brown fox jumps over the lazy dog.', 'foxjumps') == ('foxjumps', 16, 25)

#assert find_literals('The quick brown fox jumps over the lazy dog.', 'lazy') == ('lazy', 30, 34)

#assert find_literals('