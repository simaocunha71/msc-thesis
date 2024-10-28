    stack = []

    for b in brackets:
        if b == "<":
            stack.append(b)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


