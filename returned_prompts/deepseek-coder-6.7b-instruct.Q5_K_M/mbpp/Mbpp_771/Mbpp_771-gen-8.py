"""
The function can be implemented using a stack data structure. We can iterate over the expression and push the opening brackets onto the stack. When we encounter a closing bracket, we check if the stack is not empty and if the top element of the stack matches the corresponding opening bracket. If yes, we pop it from the stack, else we return False. If at the end, the stack is empty, we return True.

Here is the Python code:
"""

def check_expression(expr):
    stack = []
    brackets = {"}": "{", "]": "[", ")": "("}
    for char in expr:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return stack == []

print(check_expression("{()}[{}]"))  # True
"""
"""

