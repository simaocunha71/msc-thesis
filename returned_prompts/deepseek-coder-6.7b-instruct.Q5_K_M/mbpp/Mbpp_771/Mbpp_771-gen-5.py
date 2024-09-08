
def check_expression(exp):
    stack = [] 
    brackets = {'(': ')', '{': '}', '[': ']'}

    for char in exp:
        if char in brackets:
            stack.append(char)
        elif len(stack) == 0 or brackets[stack.pop()] != char:
            return False
    return len(stack) == 0

print(check_expression("{()}[{}]")) # True

# 3.
