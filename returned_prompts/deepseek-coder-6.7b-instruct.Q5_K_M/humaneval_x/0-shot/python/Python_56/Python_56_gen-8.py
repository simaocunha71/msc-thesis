
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            else:
                stack.pop()
    return not stack


print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False


# 10.

