    stack = []
    for c in string:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if not stack:
                return False
            stack.pop()

    return stack


