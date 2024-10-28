
def match_parens(lst):
    return 'Yes' if sum(lst[0].count('(') for _ in range(2)) == sum(lst[1].count(')') for _ in range(2)) else 'No'
