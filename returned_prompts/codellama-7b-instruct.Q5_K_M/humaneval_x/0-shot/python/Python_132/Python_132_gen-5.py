
def is_nested(string):
    brackets = {'[':']', '{':'}'}
    stack = []
    for char in string:
        if char in brackets.values():
            if stack and brackets[stack.pop()] == char:
                continue
            else:
                return False
        elif char in brackets.keys():
            stack.append(char)
    return not stack