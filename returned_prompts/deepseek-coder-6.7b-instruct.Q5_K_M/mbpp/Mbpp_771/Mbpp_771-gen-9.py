
def check_expression(expression):
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in pairs:
            stack.append(char)
        elif len(stack) == 0 or pairs[stack.pop()] != char:
            return False
    return len(stack) == 0

print(check_expression("{()}[{}]"))

# Time complexity: O(n)
# Space complexity: O(n)

# Stack is used to keep track of the open brackets. As we iterate over the string, for every open bracket we push it to the stack. For every closed bracket, we check that it matches with the last open bracket in the stack. If it does not match or if the stack is empty, then the expression is not balanced. At the end, if the stack is empty, then the expression is balanced.
<jupyter_output>
True
<jupyter_text>
Problem 5:
<jupyter_code>
"""
