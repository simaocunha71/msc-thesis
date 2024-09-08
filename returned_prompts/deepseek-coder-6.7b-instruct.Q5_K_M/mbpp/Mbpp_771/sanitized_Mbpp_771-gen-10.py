def check_expression(exp):
    stack = []
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']
    for i in exp:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if ((len(stack) > 0) and (open_brackets[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False