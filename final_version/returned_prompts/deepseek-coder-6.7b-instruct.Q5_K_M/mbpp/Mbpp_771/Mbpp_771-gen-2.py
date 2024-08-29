"""
def check_expression(expr):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
    return stack == []

assert check_expression("{()}[{}]") == True
"""

