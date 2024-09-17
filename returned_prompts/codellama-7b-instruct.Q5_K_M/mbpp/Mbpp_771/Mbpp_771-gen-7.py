
def check_expression(expression):
    stack = []
    for char in expression:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if not stack or char != {")":"(", "}":"{", "]":"["}[char]:
                return False
            stack.pop()
    return not stack


