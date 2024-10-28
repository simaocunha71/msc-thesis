    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack:
                return False
            stack.pop()

    return True if stack else False


