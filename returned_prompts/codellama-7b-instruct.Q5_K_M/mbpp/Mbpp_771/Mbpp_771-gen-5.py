
def check_expression(expression):
    if len(expression) % 2 != 0:
        return False
    stack = []
    for char in expression:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        elif char == ")" or char == "]" or char == "}":
            if len(stack) == 0:
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            elif char == "]" and top != "[":
                return False
            elif char == "}" and top != "{":
                return False
    if len(stack) != 0:
        return False
    return True


