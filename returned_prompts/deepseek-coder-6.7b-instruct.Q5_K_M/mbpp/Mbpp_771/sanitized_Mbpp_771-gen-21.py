def check_expression(expression):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in expression:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack