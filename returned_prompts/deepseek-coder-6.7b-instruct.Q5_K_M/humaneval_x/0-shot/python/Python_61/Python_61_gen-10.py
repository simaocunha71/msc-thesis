
    stack = []

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    import doctest
    doctest.testmod()


This solution uses a stack to keep track of the opening brackets. It iterates over the string, and each time it encounters an opening bracket, it adds it to the stack. When it encounters a closing bracket, it checks whether the stack is empty or its top element is not an opening bracket. If either of these conditions is true, it returns False. Otherwise, it removes the top element from the stack.

After going through all the brackets, if the stack is empty, it returns True. Otherwise, it returns False.

This solution runs in O(n) time, where n is the length of the string, as it makes a single pass over the string. It uses O(n) additional space to store the stack.


"""
from collections import deque

def correct_bracketing(brackets):
    stack = deque()
    
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack

print(correct_bracketing('('))  # False
print(correct_bracketing('()'))  # True
print(correct_bracketing('(()())'))  # True
print(correct_bracketing(')('))  # False
"""
<jupyter_output>
False
True
True
False
<jupyter_text>
