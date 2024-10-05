    stack = []
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
            if not stack:
                groups.append(''.join(stack))
                stack = []
    return groups


