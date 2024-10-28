```
def check_expression(expression):
    stack = []
    for char in expression:
        if char in ["{", "(", "["]:
            stack.append(char)
        elif char in ["}", ")", "]"]:
            if not stack or stack.pop() != match(char):
                return False
    return not stack

def match(char):
    if char == "{":
        return "}"
    elif char == "(":
        return ")"
    elif char == "[":
        return "]"
```