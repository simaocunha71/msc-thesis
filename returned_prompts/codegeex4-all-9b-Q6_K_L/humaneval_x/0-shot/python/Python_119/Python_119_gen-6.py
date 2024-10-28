def match_parens(lst):
    a = lst[0]
    b = lst[1]
    a = a + b
    b = b + a
    for i in range(len(a)):
        if a.count('(') != a.count(')'):
            return 'No'
    for i in range(len(b)):
        if b.count('(') != b.count(')'):
            return 'No'
    return 'Yes'

print(match_parens(['()(', ')'])) # == 'Yes'
print(match_parens([')', ')'])) # == 'No'