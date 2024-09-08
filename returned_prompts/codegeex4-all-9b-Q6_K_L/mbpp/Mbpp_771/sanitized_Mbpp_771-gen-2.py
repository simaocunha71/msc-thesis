def check_expression(expression):
    stack = []
    for char in expression:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack:
                return False
            if char == "}" and stack[-1] != "{":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == ")" and stack[-1] != "(":
                return False
            stack.pop()
    return not stack