
def match_parens(lst):
    s = ''.join(lst)
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        elif p == ')' and stack:
            stack.pop()
        else:
            return 'No'
    return 'Yes' if not stack else 'No'

print(match_parens(['()(', ')']))
print(match_parens([')', ')']))

# Q2:

