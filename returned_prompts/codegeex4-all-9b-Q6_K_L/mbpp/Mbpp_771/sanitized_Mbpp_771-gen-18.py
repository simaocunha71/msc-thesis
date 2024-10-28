def check_expression(exp: str) -> bool:
    stack = []
    for char in exp:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack:
                return False
            top = stack.pop()
            if (char == '}' and top != '{') or (char == ']' and top != '[') or (char == ')' and top != '('):
                return False
    return not stack