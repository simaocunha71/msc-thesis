    stack = []
    for c in lst[0] + lst[1]:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return 'No'
            stack.pop()
    return 'Yes' if not stack else 'No'  # all parentheses are balanced if stack is empty


