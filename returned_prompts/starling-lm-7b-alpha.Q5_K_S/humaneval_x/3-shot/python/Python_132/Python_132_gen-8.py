    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and len(stack) > 0:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) > 0:
        return True
    else:
        return False


