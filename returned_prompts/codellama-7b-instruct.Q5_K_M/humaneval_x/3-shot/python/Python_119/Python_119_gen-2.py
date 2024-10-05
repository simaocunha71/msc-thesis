    stack = []
    for char in lst:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return 'No'
            stack.pop()
    return 'Yes' if len(stack) == 0 else 'No'


