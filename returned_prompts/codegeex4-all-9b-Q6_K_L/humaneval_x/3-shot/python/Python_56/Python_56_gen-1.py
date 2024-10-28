    depth = 0

    for c in brackets:
        if c == '<':
            depth += 1
        elif c == '>':
            depth -= 1

        if depth < 0:
            return False

    return depth == 0


