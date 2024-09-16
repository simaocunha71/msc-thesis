def check_expression(expression):
    stack = []
    for char in expression:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if not stack:
                return False
            top = stack.pop()
            if not match(top, char):
                return False
    return not stack
def match(left, right):
    if left == "(" and right == ")":
        return True
    if left == "{" and right == "}":
        return True
    if left == "[" and right == "]":
        return True
    return False