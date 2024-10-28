    result = []

    for group in paren_string.split():
        max_depth = 0
        current_depth = 0

        for c in group:
            if c == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif c == ')':
                current_depth -= 1

        result.append(max_depth)

    return result

