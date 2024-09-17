def check_expression(expression):
    stack = []
    for char in expression:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack:
                return False
            top_element = stack.pop()
            if (char == ')' and top_element != '(') or (char == '}' and top_element != '{') or (char == ']' and top_element != '['):
                return False
    return not stack

