def check_expression(expr):
    stack = []
    opening_brackets = {'{', '(', '['}
    closing_brackets = {'}', ')', ']'}

    for char in expr:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if stack and stack.pop() not in closing_brackets:
                return False
    return len(stack) == 0