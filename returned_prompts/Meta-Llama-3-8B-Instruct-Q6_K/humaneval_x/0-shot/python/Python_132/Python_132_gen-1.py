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
                return True
    return False
```


This function works by using a stack to keep track of the brackets. When it encounters a '[', it pushes it onto the stack. When it encounters a ']', it checks if the stack is empty. If the stack is empty, it means that there is no matching '[' for the ']', so it returns True. If the stack is not empty, it pops the '[' from the stack. If the stack becomes empty at the end of the string, it means that all brackets were matched, so it returns False. 

This function assumes that the input string only contains '[' and ']'. If the string can contain other characters, you should add error checking code to handle that. 

For example, you could add a check at the beginning of the function to make sure the string only contains '[' and ']':
```
def is_nested(string):
    if any(char not in '[]' for char in string):
        return False
    # rest of the function remains the same
```


This code will return False for any string that contains a character that is not '[' or ']'.  If you want to allow other characters in the string, but still want to return False if there is no nested bracket, you could add a check at the end of the function:
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
                return True
    return len(stack) > 0
```


This code will return True if there is no matching '[' for the ']', and False otherwise.  If you want to return True only if there is a nested bracket, you could add a check at the beginning of the function:
```
def is_nested(string):
    if any(char not in '[]' for char in string):
        return False
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack:
                stack.pop()
            else:
                return True
    return len(stack) > 0 and any(char == '[' for char in stack)
```


This code will return True only if there is