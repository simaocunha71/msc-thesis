
def check_expression(expression: str) -> bool:
    stack = []
    for char in expression:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if len(stack) == 0:
                return False
            top_char = stack.pop()
            if char == ")" and top_char != "(":
                return False
            if char == "}" and top_char != "{":
                return False
            if char == "]" and top_char != "[":
                return False
    if len(stack) != 0:
        return False
    else:
        return True


