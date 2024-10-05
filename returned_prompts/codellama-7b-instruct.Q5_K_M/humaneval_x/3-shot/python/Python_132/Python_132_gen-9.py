    stack = []
    for char in string:
        if char == "[" and not stack:
            stack.append(char)
        elif char == "]" and stack[-1] == "[":
            stack.pop()
        elif char == "]":
            stack.append(char)
        elif char == "[":
            stack.pop()
    return bool(stack)


