    opening_bracket = "<"
    closing_bracket = ">"

    stack = []
    for c in brackets:
        if c == opening_bracket:
            stack.append(c)
        elif c == closing_bracket:
            if stack and stack[-1] == opening_bracket:
                stack.pop()
            else:
                return False

    return len(stack) == 0


