    """
    O(n^2)
    """
    result = []
    for group in paren_string.split(' '):
        # O(n)
        level = 0
        for char in group:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
        result.append(level)
    return result
