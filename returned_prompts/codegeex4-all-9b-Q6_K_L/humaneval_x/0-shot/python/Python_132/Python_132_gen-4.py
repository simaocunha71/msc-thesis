def is_nested(string):
    stack = []
    for c in string:
        if c == '[':
            stack.append(c)
        elif stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return bool(stack)

print(is_nested('[[]]')) # ➞ True
print(is_nested('[]]]]]]][[[[[]')) # ➞ False
print(is_nested('[][]')) # ➞ False
print(is_nested('[]')) # ➞ False
print(is_nested('[[][]]')) # ➞ True
print(is_nested('[[]][[')) # ➞ True