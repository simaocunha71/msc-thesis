def check_expression(exp):
    stack = []
    for i in exp:
        if i == "{" or i == "(" or i == "[":
            stack.append(i)
        elif i == "}" or i == ")" or i == "]":
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (top == "{" and i != "}") or (top == "(" and i != ")") or (top == "[" and i != "]"):
                return False
    if len(stack) != 0:
        return False
    return True