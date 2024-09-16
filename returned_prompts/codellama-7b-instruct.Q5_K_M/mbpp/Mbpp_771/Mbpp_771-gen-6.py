def check_expression(expression):
    stack = []
    for char in expression:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if not get_match(top) == char:
                return False
    if len(stack) != 0:
        return False
    return True

def get_match(char):
    if char == "(":
        return ")"
    elif char == "{":
        return "}"
    elif char == "[":
        return "]"
    else:
        return None
