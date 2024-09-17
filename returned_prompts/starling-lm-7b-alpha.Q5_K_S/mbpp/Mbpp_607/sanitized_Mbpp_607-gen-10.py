def find_literals(s, pattern):
    '''
    Args:
        s: A string to search for a regex pattern.
        pattern: A regex pattern to search for in the string.
    Returns:
        A tuple of the matched string, start index and end index of the matched substring in the string.
    Raises:
        ValueError: If the pattern is not a string or if the pattern does not match a substring in the string.
    '''
    if not isinstance(s, str):
        raise ValueError('The input must be a string.')
    if not isinstance(pattern, str):
        raise ValueError('The pattern must be a string.')
    if not pattern:
        raise ValueError('The pattern must not be an empty string.')
    import re
    m = re.search(pattern, s)
    if not m:
        raise ValueError('The pattern must match a substring in the string.')
    return (m.group(0), m.start(), m.end())