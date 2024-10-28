def check_expression(expression):
    stack = []
    for char in expression:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack or stack.pop() != "(" + char:
                return False
    return not stack