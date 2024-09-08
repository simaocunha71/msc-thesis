def check_expression(expression):
    opening_chars = ['(', '[', '{']
    closing_chars = [')', ']', '}']
    stack = []
    
    for char in expression:
        if char in opening_chars:
            stack.append(char)
        elif char in closing_chars:
            if not stack:
                return False
            opening_char = stack.pop()
            if opening_chars.index(opening_char) != closing_chars.index(char):
                return False
    return not stack