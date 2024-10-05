
def match_parens(lst):
    if len(lst) != 2:
        return 'No'
    open_parens = 0
    for char in lst[0]:
        if char == '(':
            open_parens += 1
        elif char == ')':
            open_parens -= 1
            if open_parens < 0:
                return 'No'
    if open_parens != 0:
        return 'No'
    open_parens = 0
    for char in lst[1]:
        if char == '(':
            open_parens += 1
        elif char == ')':
            open_parens -= 1
            if open_parens < 0:
                return 'No'
    if open_parens != 0:
        return 'No'
    return 'Yes'

