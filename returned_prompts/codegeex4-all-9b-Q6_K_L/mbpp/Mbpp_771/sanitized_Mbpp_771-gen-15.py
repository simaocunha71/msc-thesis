def check_expression(expr):
    opening_brackets = ['{', '[', '(']
    closing_brackets = ['}', ']', ')']
    stack = []
    for bracket in expr:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if len(stack) == 0:
                return False
            if opening_brackets.index(stack.pop()) != closing_brackets.index(bracket):
                return False
    if len(stack) == 0:
        return True
    else:
        return False