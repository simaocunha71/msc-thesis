    result = []
    depth = 0
    for c in paren_string:
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        else:
            result.append(depth)
    return result


