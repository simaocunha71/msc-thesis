
def match_parens(lst):
    stack = []
    for item in lst:
        if item == '(':
            stack.append(item)
        elif item == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'
