def check_expression(exp):
    """
    Args:
        exp: a string of a balanced expression
    Returns:
        True if the expression is balanced, False otherwise
    """
    stack = []
    open_brackets = {'[', '{', '('}
    close_brackets = {']', '}', ')'}
    for bracket in exp:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if not (open_brackets[top] == close_brackets[bracket]):
                return False
    return len(stack) == 0