    result = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            result.append(current_depth)
        elif c == ')':
            current_depth -= 1

    return result

