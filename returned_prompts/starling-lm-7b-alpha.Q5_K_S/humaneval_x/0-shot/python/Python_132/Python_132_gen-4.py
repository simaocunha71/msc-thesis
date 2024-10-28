
def is_nested(string):
    opening = '['
    closing = ']'
    stack = []
    for char in string:
        if char == opening:
            stack.append(char)
        elif char == closing and stack:
            stack.pop()
        else:
            return True
    return False

print(is_nested('[[]]'))  # True
print(is_nested('[]]]]]]][[[[[]'))  # False
print(is_nested('[][]'))  # False
print(is_nested('[]'))  # False
print(is_nested('[[][]]'))  # True
print(is_nested('[[]][['))  # True


```
