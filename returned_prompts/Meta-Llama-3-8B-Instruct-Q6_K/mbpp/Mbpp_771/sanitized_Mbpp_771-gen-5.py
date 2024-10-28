def check_expression(expression: str) -> bool:
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in expression:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return not stack