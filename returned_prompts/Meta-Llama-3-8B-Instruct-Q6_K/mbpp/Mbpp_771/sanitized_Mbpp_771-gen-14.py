def check_expression(expression):
    stack = []
    bracket_map = {"(": ")", "{": "}", "[": "]"}
    for bracket in expression:
        if bracket in bracket_map:
            stack.append(bracket)
        elif len(stack) == 0 or bracket_map[stack.pop()] != bracket:
            return False
    return len(stack) == 0