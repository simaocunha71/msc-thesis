    stack = []

    for c in lst:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return 'No'
            stack.pop()

    if stack:
        return 'No'

    return 'Yes'


