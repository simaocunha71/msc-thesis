    result = []
    for group in paren_string.split():
        stack = []
        max_depth = 0
        current_depth = 0
        for c in group:
            if c == '(':
                current_depth += 1
                stack.append(c)
                if current_depth > max_depth:
                    max_depth = current_depth
            elif c == ')':
                current_depth -= 1
                stack.pop()
        result.append(max_depth)
    return result


