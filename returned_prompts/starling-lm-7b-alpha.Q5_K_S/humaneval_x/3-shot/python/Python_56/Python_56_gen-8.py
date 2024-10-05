    opening_brackets = "><"
    closing_brackets = "<<>"
    stack = []

    for c in brackets:
        if c in opening_brackets:
            stack.append(c)
        elif c in closing_brackets:
            if stack:
                if opening_brackets.index(c) != closing_brackets.index(stack[-1]):
                    return False
                stack.pop()
            else:
                return False

    return not stack


