    stack = []
    for c in string:
        if c == '[':
            stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False

    return not stack

