
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

# Test cases
print(is_nested('[[]]'))  # True
print(is_nested('[]]]]]]][[[[[]'))  # False
print(is_nested('[][]'))  # False
print(is_nested('[]'))  # False
print(is_nested('[[][]]'))  # True
print(is_nested('[[]][['))  # True



# Explanation:
# The function `is_nested` takes a string as input, which contains only square brackets.
# It initializes an empty stack to keep track of the opening brackets encountered.
# For each character in the string, if it is an opening bracket ('['), it is added to the stack.
# If it is a closing bracket (']'), it checks if the stack is empty. If the stack is empty,
# it means there is no valid subsequence of brackets with nested brackets, so it returns True.
# If the stack is not empty, it means there is at least one bracket that is nested,
# so it pops the topmost opening bracket from the stack.
# After processing all characters in the string, if the stack is empty, it means there are no nested brackets,
# so it returns False. Otherwise, it returns True, indicating the presence of at least one nested bracket.



# Time Complexity: O(n), where n is the length of the input string.
# This is because the function iterates over the string once, and the number of iterations is proportional to the length of the string.

# Space Complexity: O(n), where n is the length of the input string.
# This is because the function uses a stack to keep track of the opening brackets encountered, and the maximum size of the stack is determined by the length of the input string.

```python

```