def check_expression(expression):
    stack = []
    for char in expression:
        if char in ["(", ")", "{", "}", "[", "]"]:
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            elif char == ")" and stack[-1] != ")":
                return False
            elif char == "}" and stack[-1] != "}":
                return False
            elif char == "]" and stack[-1] != "]":
                return False
            else:
                stack.pop()
    return len(stack) == 0