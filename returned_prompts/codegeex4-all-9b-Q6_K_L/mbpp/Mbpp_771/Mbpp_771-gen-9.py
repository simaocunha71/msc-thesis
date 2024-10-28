def check_expression(expression: str) -> bool:
    opening_brackets = ['{', '(', '[']
    closing_brackets = ['}', ')', ']']

    stack = []

    for bracket in expression:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(bracket):
                return False

    return len(stack) == 0

