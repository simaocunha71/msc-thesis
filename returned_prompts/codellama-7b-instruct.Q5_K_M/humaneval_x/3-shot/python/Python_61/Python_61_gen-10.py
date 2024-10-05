    stack = []

    for char in brackets:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0


