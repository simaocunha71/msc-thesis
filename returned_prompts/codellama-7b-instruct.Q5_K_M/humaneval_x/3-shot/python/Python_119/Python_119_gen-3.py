    stack = []
    for char in lst[0] + lst[1]:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return 'No'
            stack.pop()

    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'


