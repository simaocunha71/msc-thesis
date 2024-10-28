def check_expression(expression: str) -> bool:
    stack = []
    for char in expression:
        if char == "{" or char == "[" or char == "(":
            stack.append(char)
        elif char == "}" or char == "]" or char == ")":
            if not stack:
                return False
            top = stack.pop()
            if (top == "{" and char != "}") or (top == "[" and char != "]") or (top == "(" and char != ")"):
                return False
    return not stack