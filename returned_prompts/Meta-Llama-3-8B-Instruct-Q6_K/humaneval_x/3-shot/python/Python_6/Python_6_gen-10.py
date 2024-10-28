    result = []
    current_level = 0

    for c in paren_string:
        if c == '(':
            current_level += 1
        elif c == ')':
            current_level -= 1
        else:
            result.append(current_level)
            current_level = 0

    return result


