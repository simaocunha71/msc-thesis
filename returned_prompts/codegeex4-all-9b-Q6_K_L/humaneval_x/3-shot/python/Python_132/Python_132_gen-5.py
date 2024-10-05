    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0