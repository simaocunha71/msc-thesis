"""
Here is a possible solution to the problem:

"""

from collections import deque

def check_expression(expression):
    stack = deque()
    for char in expression:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if not stack:
                return False
            elif (")" == char and stack[-1] != ")"):
                return False
            elif "]" == char and stack[-1] != "]"):
                return False
            elif "}" == char and stack[-1] != "}"):
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

# Tests
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[}")] == False
assert check_expression("{()}[}")] == False

"""
The function uses a stack to check the expression's balance.

The stack is initialized as an empty deque (a double-ended queue).

The input expression is iterated through one character at a time.
If the current character is an opening bracket (i.e., "(", "{", or "["),
then it is added to the stack.
If the current character is a closing bracket (i.e., ")", "]", or "}"),
then the stack is checked. If the stack is empty, this means that the opening bracket has no match, so the expression is not balanced.
If the stack is not empty but the current character does not match the top element in the stack, this means that the opening bracket has a mismatched closing bracket, so the expression is not balanced.
If the stack is not empty and the current character matches the top element in the stack, then the top element in the stack is removed from the stack.
Once the entire expression has been iterated through, the stack is checked. If the stack is not empty, this means that there are some opening brackets without matching closing brackets, so the expression is not balanced.
If the stack is empty, then the expression is balanced and the function returns True. Otherwise, the expression is not balanced and the function returns