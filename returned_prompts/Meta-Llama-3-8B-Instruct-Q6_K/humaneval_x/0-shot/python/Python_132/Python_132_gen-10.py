```
def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) > 0
```
This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty. If it is, it means there's no matching opening bracket, so it returns False. If the stack is not empty, it pops the opening bracket from the stack. After going through the entire string, it checks if the stack is not empty. If it's not empty, it means there are unmatched opening brackets, so it returns True. If the stack is empty, it means all brackets are matched, so it returns False. This function works because a bracket is nested if and only if it has a matching opening bracket that is not closed until the current bracket is closed. The stack keeps track of these opening brackets, so we can check if a bracket is nested by checking if its matching opening bracket is still on the stack when we encounter the closing bracket.