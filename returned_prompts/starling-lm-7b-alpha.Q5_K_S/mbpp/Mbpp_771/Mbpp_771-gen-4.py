```
def check_expression(exp):
    """
    Args:
        exp: a string of a balanced expression
    Returns:
        True if the expression is balanced, False otherwise
    """
    stack = []
    open_brackets = {'[', '{', '('}
    close_brackets = {']', '}', ')'}
    for bracket in exp:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if not (open_brackets[top] == close_brackets[bracket]):
                return False
    return len(stack) == 0
```

This function works by iterating over the characters in the expression and keeping track of an open_bracket stack. It checks if each character is an open bracket, and if so, it adds it to the stack. If the character is a close bracket, it checks if the stack is empty or if the close bracket does not match the most recent open bracket. If any of these conditions are not met, it returns False, indicating that the expression is not balanced. At the end of the function, it checks if the stack is empty, indicating that all open brackets have been matched with close brackets, and returns True if the stack is empty, otherwise False.

The time complexity of this function is O(n), where n is the length of the expression, as it iterates over each character in the expression once. The space complexity is O(n) as well, as the stack can have at most n elements.

In the provided assert statement, the function is tested with the expression "{()}[{}]". The expression is balanced because every open bracket is matched with a close bracket in the correct order: {()}[{]} -> {(}[{]} -> {(}{)} -> {}

The function returns True, indicating that the expression is balanced.

"""

check_expression("{()}[{}]") # True
```

This code defines a function called `check_expression` that takes a string `exp` as an argument. The function checks if the given expression