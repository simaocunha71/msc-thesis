def check_expression(expr):
    stack = []
    brackets = {"}": "{", "]": "[", ")": "("}
    for char in expr:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return stack == []