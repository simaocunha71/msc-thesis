    stack = []
    for c in string:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack:
                stack.pop()
            else:
                return True
    return False


