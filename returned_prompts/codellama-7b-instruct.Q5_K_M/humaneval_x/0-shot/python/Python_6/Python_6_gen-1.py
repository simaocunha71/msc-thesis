def parse_nested_parens(paren_string):
    """
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    depth = []
    for c in paren_string:
        if c == '(':
            stack.append(c)
            depth.append(len(stack))
        elif c == ')':
            stack.pop()
            depth.pop()
    return [max(depth)]


