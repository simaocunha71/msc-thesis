
def match_parens(lst):
    return 'Yes' if (lst[0] + lst[1]).count('(') % 2 == 0 else 'No'
