def match_parens(lst):
    s = ''.join(lst)
    open_parens = 0
    for char in s:
        if char == '(':
            open_parens += 1
        else:
            open_parens -= 1
        if open_parens < 0:
            return 'No'
    return 'Yes' if open_parens == 0 else 'No'

print(match_parens(['()(', ')']))  # 'Yes'
print(match_parens([')', ')']))  # 'No'
print(match_parens(['(', ')']))  # 'No'
print(match_parens(['(', '(', ')', ')']))  # 'Yes'