Opening and closing brackets are said to be correctly bracketed if every opening bracket has a corresponding closing bracket, and the closing bracket comes after the opening one in the string. Here are some examples of correct bracketing:

```
""
"()"
"(()())"
"(())((()))"
```

And here are some examples of incorrect bracketing:

```
")("
"("
")()()"
```

To solve the problem, initialize a stack and an index. Iterate over the string. If the character at the current index is an opening bracket, push it to the stack. If the character is a closing bracket, pop the stack. If the stack is empty at the end, return True. Otherwise, return False.

Here is a Python implementation of the solution:

```python
def correct_bracketing(brackets):
    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
```

The time complexity of this solution is O(n), where n is the length of the string.































































































































































































































