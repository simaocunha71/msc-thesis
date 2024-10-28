def is_nested(string):
    if len(string) <= 1:
        return False
    if string[0] != '[' or string[-1] != ']':
        return False
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

print(is_nested('[[]]')) # True
print(is_nested('[]]]]]]][[[[[]')) # False
print(is_nested('[][]')) # False
print(is_nested('[]')) # False
print(is_nested('[[][]]')) # True
print(is_nested('[[]][[')) # True
print(is_nested('[[[[]]]]]]]]][]')) # False
print(is_nested('[[[[]]]]]]]]][]')) # False