    result = []
    current_depth = 0
    current_max_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_max_depth = max(current_depth, current_max_depth)
        elif c == ')':
            current_depth -= 1

        if c == ' ':
            result.append(current_max_depth)
            current_depth = 0
            current_max_depth = 0

    return result


