    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        else:
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
                return True
    return False


