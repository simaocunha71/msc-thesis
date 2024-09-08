def check_expression(expr):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expr:
        if char in brackets:
            stack.append(char)
        elif len(stack) == 0 or brackets[stack.pop()] != char:
            return False
    return len(stack) == 0