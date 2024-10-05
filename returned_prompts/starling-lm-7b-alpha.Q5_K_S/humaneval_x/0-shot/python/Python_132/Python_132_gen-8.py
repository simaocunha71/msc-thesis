
def is_nested(string):
    open_brackets = 0
    for bracket in string:
        if bracket == '[':
            open_brackets += 1
        elif bracket == ']':
            open_brackets -= 1
        if open_brackets < 0:
            return True
    return open_brackets == 0


# Test cases
print(is_nested('[[]]'))  # True
print(is_nested('[]]]]]]][[[[[]'))  # False
print(is_nested('[][]'))  # False
print(is_nested('[]'))  # False
print(is_nested('[[][]]'))  # True
print(is_nested('[[]][['))  # True



