
def match_parens(lst):
    if lst[0].count('(') == lst[1].count('(') and lst[0].count(')') == lst[1].count(')'):
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')'])) # 'Yes'
print(match_parens([')', ')'])) # 'No'



