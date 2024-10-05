    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if not stack:
                return False
            stack.pop()
    return True if stack else False


