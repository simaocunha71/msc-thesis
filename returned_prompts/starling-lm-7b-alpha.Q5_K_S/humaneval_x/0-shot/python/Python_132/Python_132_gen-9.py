
def is_nested(string):
    stack = []
    for ch in string:
        if ch == '[':
            stack.append(ch)
        elif ch == ']':
            if not stack:
                return False
            stack.pop()
    return len(stack) > 0


# Test Cases
print(is_nested('[[]]'))  # True
print(is_nested('[]]]]]]][[[[[]'))  # False
print(is_nested('[][]'))  # False
print(is_nested('[]'))  # False
print(is_nested('[[][]]'))  # True
print(is_nested('[[]][['))  # True

```
