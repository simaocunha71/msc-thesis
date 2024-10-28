def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return True
    return False

print(is_nested('[[]]')) # ➞ True
print(is_nested('[]]]]]]][[[[[]')) # ➞ False
print(is_nested('[][]')) # ➞ False
print(is_nested('[]')) # ➞ False
print(is_nested('[[][]]')) # ➞ True
print(is_nested('[[]][[')) # ➞ True