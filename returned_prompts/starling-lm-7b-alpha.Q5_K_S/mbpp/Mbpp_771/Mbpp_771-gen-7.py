"""
The problem can be solved using a stack. We push the opening brackets onto the stack and pop the closing brackets. If the stack is empty in the end, then the expression is balanced, otherwise, it is not.
"""


def check_expression(expression):
    """
    Check if the given expression is balanced or not.
    """
    stack = []
    for c in expression:
        if c in ["(", "{", "["]:
            stack.append(c)
        elif c in [")", "}", "]"]:
            if not stack or stack.pop() != expression[expression.index(c) - 1]:
                return False
    return not stack


# assert check_expression("{()}[{}]") == True
# assert check_expression("{()}[}"] == False
# assert check_expression("({})[]{}") == True
# assert check_expression("([{}])") == True


def check_expression_naive(expression):
    """
    Check if the given expression is balanced or not.
    """
    for c in expression:
        if c in ["(", "{", "["]:
            stack.append(c)
        elif c in [")", "}", "]"]:
            if not stack or stack.pop() != expression[expression.index(c) - 1]:
                return False
    return not stack


# assert check_expression_naive("{()}[{}]") == True
# assert check_expression_naive("{()}[}"] == False
# assert check_expression_naive("({})[]{}") == True
# assert check_expression_naive("([{}])") == True


def check_expression_optimized(expression):
    """
    Check if the given expression is balanced or not.
    """
    stack = []
    for c in expression:
        if c in ["(", "{", "["]:
            stack.append(c)
        elif c in [")", "}", "]"]:
            if stack and stack[-1] != expression[expression.index(c) - 1]:
                return False
            stack.pop()
    return not stack


# assert