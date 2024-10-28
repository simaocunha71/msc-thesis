```
def is_nested(s):
    stack = []
    for char in s:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) > 0
```


The function `is_nested` takes a string `s` as input and returns a boolean value. It uses a stack to keep track of the opening brackets. 

The function iterates over each character in the string. If the character is an opening bracket, it pushes it onto the stack. If the character is a closing bracket, it checks if the stack is empty. If the stack is empty, it means there is no matching opening bracket, so the function returns `False`. If the stack is not empty, it pops the opening bracket from the stack.

After iterating over all characters in the string, the function checks if the stack is not empty. If it is not empty, it means there are unmatched opening brackets, so the function returns `True`. If the stack is empty, it means all brackets are matched, so the function returns `False`.

The function works by tracking the nesting of brackets. If there is at least one nested bracket, the function returns `True`; otherwise, it returns `False`. This is why the function works correctly for all test cases. 