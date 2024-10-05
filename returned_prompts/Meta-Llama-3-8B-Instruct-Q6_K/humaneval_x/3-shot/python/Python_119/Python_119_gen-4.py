    stack = []
    for parenthesis in lst[0] + lst[1]:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif parenthesis == ')':
            if not stack:
                return 'No'
            stack.pop()
    if not stack:
        return 'Yes'
    return 'No'  # Stack is not empty, so it's not a good string


