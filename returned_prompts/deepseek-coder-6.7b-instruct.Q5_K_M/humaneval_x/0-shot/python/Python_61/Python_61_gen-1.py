
```python
def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return not stack

print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
```

This solution uses a stack to track the opening brackets. When it encounters a closing bracket, it checks whether the stack is empty or the last bracket on the stack is not an opening bracket. If either of these conditions is true, it returns False. Otherwise, it pops the last bracket from the stack. If the stack is empty after traversing the entire string of brackets, it returns True. Otherwise, it returns False. This is because every opening bracket should have a corresponding closing bracket. If there are any unmatched opening brackets left in the stack, it means that there are unmatched closing brackets, and it returns False.

This solution has a time complexity of O(n) and a space complexity of O(n) where n is the number of brackets.
"""

# ---------------------
"""
