    stack = []
    for c in lst[0] + lst[1]:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()

    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'


