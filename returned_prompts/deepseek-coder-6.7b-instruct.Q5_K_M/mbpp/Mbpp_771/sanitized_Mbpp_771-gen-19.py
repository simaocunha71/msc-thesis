def check_expression(expr):
    stack = []
    p_map = {'(': ')', '{': '}', '[': ']'}
    for char in expr:
        if char in p_map:
            stack.append(char)
        elif len(stack) == 0 or p_map[stack.pop()] != char:
            return False
    return len(stack) == 0