    result = []
    current_depth = 0
    max_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif c == ')':
            current_depth -= 1

        if c == ' ':
            result.append(max_depth)
            current_depth = 0
            max_depth = 0

    if max_depth > 0:
        result.append(max_depth)

    return result

