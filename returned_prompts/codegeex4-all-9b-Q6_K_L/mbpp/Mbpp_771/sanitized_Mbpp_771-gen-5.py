def check_expression(expression: str) -> bool:
    """Check if the given expression is balanced or not."""
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif stack and brackets[stack[-1]] == char:
            stack.pop()
        else:
            return False
    return not stack