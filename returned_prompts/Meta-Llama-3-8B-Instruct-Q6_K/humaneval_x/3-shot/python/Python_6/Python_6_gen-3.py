    result = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
        elif c == ')':
            current_depth -= 1
            result.append(current_depth)
        if c == ' ':
            result.append(current_depth)
            current_depth = 0

    return result


