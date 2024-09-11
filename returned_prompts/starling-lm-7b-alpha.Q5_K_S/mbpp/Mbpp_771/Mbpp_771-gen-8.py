"""
def check_expression(expression):
    stack = []
    for c in expression:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if len(stack) == 0:
                return False
            elif (c == ')' and stack[-1] != '{') or (c == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True
"""

def check_expression(expression):
    stack = []
    for c in expression:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if stack == []:
                return False
            elif (c == ')' and stack[-1] != '{') or (c == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop()

    if stack == []:
        return True
    else:
        return False

# assert check_expression("{()}[{}]") == True
# assert check_expression("{()}[}"] == False
# assert check_expression("(]") == False
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])") == True
# assert check_expression("([{}])")