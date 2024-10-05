def is_nested(string):
    count = 0
    for c in string:
        if c == '[':
            count += 1
        elif c == ']':
            count -= 1
            if count < 0:
                return False
    return count == 0

print(is_nested('[[]]')) #➞ True
print(is_nested('[]]]]]]][[[[[]')) #➞ False
print(is_nested('[][]')) #➞ False
print(is_nested('[]')) #➞ False
print(is_nested('[[][]]')) #➞ True
print(is_nested('[[]][[')) #➞ True