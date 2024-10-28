def check_expression(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}

    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif len(stack) == 0 or brackets[stack.pop()] != char:
            return False
    return len(stack) == 0