
def match_parens(lst):
    parens_count = 0
    for char in lst:
        if char == '(':
            parens_count += 1
        elif char == ')':
            parens_count -= 1
        if parens_count < 0:
            return 'No'
    if parens_count == 0:
        return 'Yes'
    else:
        return 'No'
