def check_expression(s: str) -> bool:
    stack = []
    expression = {'(': ')', '{': '}', '[': ']'}
    for i in s:
        if i in expression.values():
            if len(stack) == 0:
                return False
            if stack.pop() != expression[i]:
                return False
        elif i in expression.keys():
            stack.append(i)
    return len(stack) == 0