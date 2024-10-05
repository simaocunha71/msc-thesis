```
def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack or stack.pop() != "<":
                return False
    return not stack
```
This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty or if the top of the stack doesn't match the closing bracket. If either of these conditions is true, it returns `False`. If it iterates through the entire string without returning `False`, it returns `not stack`, which is `True` if the stack is empty (i.e., every opening bracket had a corresponding closing bracket) and `False` otherwise.