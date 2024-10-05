    result = []
    current_depth = 0
    current_string = ''

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string += c
        elif c == ')':
            current_depth -= 1
            current_string += c
            if current_depth == 0:
                result.append(current_depth)
                current_string = ''

    return result


