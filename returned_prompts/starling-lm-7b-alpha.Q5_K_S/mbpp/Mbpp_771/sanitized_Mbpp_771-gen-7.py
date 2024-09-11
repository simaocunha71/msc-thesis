def check_expression(expression):
    """
    Check if the given expression is balanced or not.
    """
    stack = []
    for c in expression:
        if c in ["(", "{", "["]:
            stack.append(c)
        elif c in [")", "}", "]"]:
            if not stack or stack.pop() != expression[expression.index(c) - 1]:
                return False
    return not stack