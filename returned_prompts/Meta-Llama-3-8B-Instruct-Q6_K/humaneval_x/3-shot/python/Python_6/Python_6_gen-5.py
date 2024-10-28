    result = []
    current_level = 0

    for c in paren_string.split():
        if c == '(':
            current_level += 1
        elif c == ')':
            current_level -= 1
        result.append(current_level)

    return result


