
    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
