def check_expression(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack == [] or stack.pop() != pairs[char]:
                return False
    return stack == []