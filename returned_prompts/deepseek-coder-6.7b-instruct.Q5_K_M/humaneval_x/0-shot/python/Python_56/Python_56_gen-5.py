
    stack = []

    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            if not stack:
                return False
            stack.pop()

    return not stack


print(correct_bracketing("<"))  # False
print(correct_bracketing("<>"))  # True
print(correct_bracketing("<<><>>"))  # True
print(correct_bracketing("><<>"))  # False
"""

# Task 2

"""
