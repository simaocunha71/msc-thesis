    result = []

    for group in paren_string.split():
        level = 0
        for c in group:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1

        result.append(level)

    return result


