    result = []
    current_depth = 0
    stack = []

    for c in paren_string:
        if c == '(':
            stack.append(c)
            current_depth += 1
        elif c == ')':
            stack.pop()
            current_depth -= 1

        result.append(current_depth)

    return result
# 