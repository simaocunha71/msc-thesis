def check_expression(exp):
    stack = []
    pairs = {'}': '{', ']': '[', ')': '('}
    for char in exp:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack