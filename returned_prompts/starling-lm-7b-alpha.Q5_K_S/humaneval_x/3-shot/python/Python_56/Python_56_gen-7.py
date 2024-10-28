    opening_brackets = "([{"
    closing_brackets = ")]}"
    stack = []

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if stack and opening_brackets.index(stack[-1]) + 1 != closing_brackets.index(bracket):
                return False
            stack.pop()

    return not stack


