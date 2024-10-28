def check_expression(expr):
    stack = []
    open_t = ["[","{","("] 
    close_t = ["]","}",")"] 
    for i in expr:
        if i in open_t:
            stack.append(i)
        elif i in close_t:
            pos = close_t.index(i)
            if ((len(stack) > 0) and
                (open_t[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False