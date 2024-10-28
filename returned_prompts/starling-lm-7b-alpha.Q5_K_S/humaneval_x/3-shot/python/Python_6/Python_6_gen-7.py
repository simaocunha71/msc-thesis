    result = []
    current_depth = 0
    for c in paren_string:
        if c == '(':
            current_depth += 1
        elif c == ')':
            current_depth -= 1

        if c == ')':
            result.append(current_depth)

    return result


