def check_expression(expression):
    stack = []
    for char in expression:
        if char == "{":
            stack.append(char)
        elif char == "}":
            if len(stack) == 0:
                return False
            stack.pop()
        elif char == "[":
            stack.append(char)
        elif char == "]":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0