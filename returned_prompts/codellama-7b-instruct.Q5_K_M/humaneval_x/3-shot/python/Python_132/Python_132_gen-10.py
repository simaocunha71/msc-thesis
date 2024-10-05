    stack = []

    for s in string:
        if s == '[':
            stack.append(s)
        elif s == ']':
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) > 0


