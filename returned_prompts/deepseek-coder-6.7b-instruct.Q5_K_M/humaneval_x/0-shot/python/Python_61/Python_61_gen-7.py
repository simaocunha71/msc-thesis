
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


print(correct_bracketing("("))
print(correct_bracketing("()"))
print(correct_bracketing("(()())"))
print(correct_bracketing(")(()"))
"""

# Task 2

"""
