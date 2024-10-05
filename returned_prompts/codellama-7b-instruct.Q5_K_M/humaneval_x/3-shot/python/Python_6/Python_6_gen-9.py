    result = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
        elif c == ')':
            current_depth -= 1

            if current_depth > result[-1]:
                result.append(current_depth)

    result.pop()

    return result


