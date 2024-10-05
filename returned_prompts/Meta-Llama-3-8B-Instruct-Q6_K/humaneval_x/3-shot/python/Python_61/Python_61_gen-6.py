    stack = []

    for c in brackets:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()

    return not stack


