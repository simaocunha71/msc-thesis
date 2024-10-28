    stack = []
    groups = []
    for paren in paren_string:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            if len(stack) == 0:
                raise SyntaxError('Unbalanced parentheses')
            stack.pop()
            if len(stack) == 0:
                groups.append(''.join(stack))
                stack = []
    if len(stack) != 0:
        raise SyntaxError('Unbalanced parentheses')
    return groups


