    stack = []
    for ch in string:
        if ch == '[':
            stack.append(ch)
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return any(stack)


