"""
def check_expression(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack == [] or pairs[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

print(check_expression("{()}[{}]"))
"""

