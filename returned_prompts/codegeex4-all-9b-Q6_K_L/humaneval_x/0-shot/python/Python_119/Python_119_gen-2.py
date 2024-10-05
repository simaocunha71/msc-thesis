def match_parens(lst):
    s = ''.join(lst)
    return 'Yes' if s.count('(') == s.count(')') else 'No'

print(match_parens(['()(', ')']))
print(match_parens([')', ')']))