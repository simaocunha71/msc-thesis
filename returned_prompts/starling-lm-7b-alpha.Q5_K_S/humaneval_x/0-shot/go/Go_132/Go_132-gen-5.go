
Here is a Python solution to the problem:

```python
def IsNested(s):
    # Create a stack to store the opening brackets
    stack = []

    # Traverse through the string
    for i in range(len(s)):
        # If the current character is an opening bracket
        if s[i] == '[':
            # Push the character to the stack
            stack.append(s[i])
        # If the current character is a closing bracket
        elif s[i] == ']':
            # If the stack is empty, there are no nested brackets
            if len(stack) == 0:
                return False
            # If the last character in the stack is an opening bracket,
            # then pop it from the stack.
            # Otherwise, there are no nested brackets
            elif stack[-1] != '[':
                return False
            # Otherwise, pop the character from the stack
            else:
                stack.pop()
    # If the stack is not empty, there are nested brackets
    if len(stack) != 0:
        return True
    # Otherwise, there are no nested brackets
    return False
```

To use the function, you can do the following:

```python
print(IsNested('[[]]'))  # true
print(IsNested('[]]]]]]][[[[[]'))  # false
print(IsNested('[][]'))  # false
print(IsNested('[]'))  # false
print(IsNested('[[][]]'))  # true
print(IsNested('[[]][['))  # true
```

The function works by traversing through the string and keeping track of the opening brackets using a stack. If the current character is an opening bracket, it is pushed to the stack. If the current character is a closing bracket, the function checks if the stack is empty or if the last character in the stack is an opening bracket. If either of these conditions is true, the function returns False, indicating that there are no nested brackets. If the last character in the stack is not an opening bracket, the function also returns False. If the