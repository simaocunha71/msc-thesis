def find_literals(s, pattern):
    '''
    Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
    '''
    import re
    result = re.search(pattern, s)
    return result.group(), result.start(), result.end()