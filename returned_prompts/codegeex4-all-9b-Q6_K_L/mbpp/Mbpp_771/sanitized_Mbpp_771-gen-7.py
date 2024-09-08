def check_expression(expression):
    stack = []
    for char in expression:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if not stack:
                return False
            opening = stack.pop()
            if (opening == "{" and char != "}") or (opening == "[" and char != "]") or (opening == "(" and char != ")"):
                return False
    return not stack