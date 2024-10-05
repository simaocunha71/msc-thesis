
def is_nested(string):
    if '[' not in string or ']' not in string:
        return False
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack:
                return False
            stack.pop()
    return not stack