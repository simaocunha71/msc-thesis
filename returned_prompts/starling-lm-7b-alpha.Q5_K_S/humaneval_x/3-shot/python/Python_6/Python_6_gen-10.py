    result = []
    for group in paren_string.split(' '):
        depth = 0
        for c in group:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1

            if depth > result[-1]:
                result.append(depth)

    return result


