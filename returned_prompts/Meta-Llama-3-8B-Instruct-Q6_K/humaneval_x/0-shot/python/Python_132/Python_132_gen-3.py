```
def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack:
                stack.pop()
            else:
                return False
    return bool(stack)
```
This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is not empty. If the stack is not empty, it pops the opening bracket from the stack. If the stack is empty, it means there is no corresponding opening bracket for the closing bracket, so it returns False. At the end of the function, it checks if the stack is empty. If the stack is not empty, it means there are unbalanced opening brackets, so it returns True. If the stack is empty, it means all brackets are balanced, so it returns False. 