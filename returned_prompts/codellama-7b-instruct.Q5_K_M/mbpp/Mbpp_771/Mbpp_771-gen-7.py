```python
def check_expression(expression):
    open_brackets = ["[", "{", "("]
    close_brackets = ["]", "}", ")"]
    stack = []

    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or stack.pop() != open_brackets[close_brackets.index(char)]:
                return False

    return not stack
```