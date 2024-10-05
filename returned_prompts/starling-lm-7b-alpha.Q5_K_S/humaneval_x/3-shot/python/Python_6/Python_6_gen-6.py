    def max_depth(parens):
        result = 0
        current_depth = 0
        for c in parens:
            if c == '(':
                current_depth += 1
                result = max(result, current_depth)
            elif c == ')':
                current_depth -= 1
        return result

    result = []
    for group in paren_string.split():
        result.append(max_depth(group))

    return result


