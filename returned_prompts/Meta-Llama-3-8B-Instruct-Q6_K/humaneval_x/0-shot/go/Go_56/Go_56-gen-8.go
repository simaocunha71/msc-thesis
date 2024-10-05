```
def CorrectBracketing(brackets):
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append("<")
        elif bracket == ">":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
```


Python code that uses a stack to check if every opening bracket has a corresponding closing bracket. It iterates over the string, pushing opening brackets onto the stack and popping them off when it encounters a closing bracket. If it ever encounters a closing bracket when the stack is empty, it returns False. If the stack is not empty after it has finished iterating over the string, it returns False. If it has not returned False by the end, it returns True, indicating that every opening bracket had a corresponding closing bracket.