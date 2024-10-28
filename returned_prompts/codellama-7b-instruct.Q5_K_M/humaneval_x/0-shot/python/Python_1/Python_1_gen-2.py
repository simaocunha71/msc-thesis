    stack = []
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        if len(stack) == 0:
            groups.append(''.join(stack))
            stack = []
    return groups