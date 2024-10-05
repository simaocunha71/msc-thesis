    result = []
    current_depth = 0
    max_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif c == ')':
            current_depth -= 1

        if c == ' ' or c == ')':
            result.append(max_depth)
            max_depth = 0

    return result


