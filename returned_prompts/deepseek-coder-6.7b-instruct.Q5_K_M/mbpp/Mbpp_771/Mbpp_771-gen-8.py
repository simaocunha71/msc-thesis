
def check_expression(expr):
    stack = []
    p_dict = {'(': ')', '{': '}', '[': ']'}

    for char in expr:
        if char in p_dict:
            stack.append(char)
        elif len(stack) == 0 or p_dict[stack.pop()] != char:
            return False
    return len(stack) == 0


