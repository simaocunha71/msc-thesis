def check_expression(expression):
    stack = []
    mapping = {"(": ")", "[": "]", "{": "}"}
    for char in expression:
        if char in mapping:
            stack.append(char)
        elif len(stack) == 0 or mapping[stack.pop()] != char:
            return False
    return len(stack) == 0