
def check_expression(exp: str) -> bool:
    stack = []
    for char in exp:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if not is_balanced(top, char):
                return False
    return len(stack) == 0

def is_balanced(open_char, close_char):
    if open_char == "(" and close_char == ")":
        return True
    elif open_char == "{" and close_char == "}":
        return True
    elif open_char == "[" and close_char == "]":
        return True
    else:
        return False


