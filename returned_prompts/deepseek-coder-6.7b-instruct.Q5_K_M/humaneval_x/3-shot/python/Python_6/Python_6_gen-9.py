    result = []
    for group in paren_string.split():
        current_depth = 0
        max_depth = 0
        for c in group:
            if c == '(':
                current_depth += 1
            elif c == ')':
                current_depth -= 1
            max_depth = max(max_depth, current_depth)
        result.append(max_depth)
    return result


