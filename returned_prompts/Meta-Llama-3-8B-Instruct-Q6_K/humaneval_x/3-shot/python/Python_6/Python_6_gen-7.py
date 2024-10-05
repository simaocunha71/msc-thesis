    result = []
    current_depth = 0

    for c in paren_string.split():
        if c == '(':
            current_depth += 1
        elif c == ')':
            current_depth -= 1
        else:
            result.append(current_depth)
            current_depth = 0

    return result


