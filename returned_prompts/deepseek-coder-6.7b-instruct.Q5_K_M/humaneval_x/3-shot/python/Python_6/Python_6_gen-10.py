    result = []

    for group in paren_string.split():
        current_depth = max_depth = 0

        for char in group:
            if char == "(":
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ")":
                current_depth -= 1

        result.append(max_depth)

    return result


