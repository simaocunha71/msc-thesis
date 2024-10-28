    depth = 0
    for char in string:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

