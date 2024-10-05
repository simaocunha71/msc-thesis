    result = []
    for paren_string in paren_string.split(' '):
        level = 0
        max_level = 0
        for c in paren_string:
            if c == '(':
                level += 1
                max_level = max(max_level, level)
            elif c == ')':
                level -= 1
        result.append(max_level)

    return result
