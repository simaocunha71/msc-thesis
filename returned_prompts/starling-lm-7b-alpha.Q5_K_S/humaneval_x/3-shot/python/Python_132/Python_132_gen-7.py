    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']' and stack:
            stack.pop()
        else:
            return True
    return False


