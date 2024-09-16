```
def check_expression(expression):
    stack = []
    for char in expression:
        if char == "{" or char == "(" or char == "[":
            stack.append(char)
        elif char == "}" or char == ")" or char == "]":
            if len(stack) == 0:
                return False
            top = stack.pop()
            if char == "}" and top != "{" or char == ")" and top != "(" or char == "]" and top != "[":
                return False
    return len(stack) == 0
```
