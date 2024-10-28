
```python
def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack or stack.pop() != "(":
                return False
    return not stack
```

This function uses a stack to keep track of the opening brackets that have not been closed yet. It iterates through the string, adding opening brackets to the stack and popping the last item from the stack when it encounters a closing bracket. If at any point the stack is empty (indicating that there is no matching opening bracket for the current closing bracket) or the last item in the stack is not an opening bracket, it returns False. If it successfully iterates through the entire string without returning, it returns True.

This solution has a time complexity of O(n) and a space complexity of O(n) because it iterates through the string once and uses a stack to keep track of the opening brackets.

The time complexity is O(n) because we are iterating through the string once. The space complexity is O(n) because in the worst case scenario (when every opening bracket has a corresponding closing bracket), we will be storing all the opening brackets in the stack.

In summary, this function correctly determines if every opening bracket has a corresponding closing bracket in the given string.
"""

# 