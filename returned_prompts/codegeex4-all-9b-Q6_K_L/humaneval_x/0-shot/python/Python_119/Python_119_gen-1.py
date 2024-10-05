def match_parens(lst):
    left = 0
    for char in lst[0]:
        if char == '(':
            left += 1
        else:
            left -= 1
    if left < 0:  # more ')' than '(' in lst[0]
        left = -left
        lst.reverse()
    right = 0
    for char in lst[1]:
        if char == '(':
            right += 1
        else:
            right -= 1
    if right < 0:  # more ')' than '(' in lst[1]
        right = -right
    if left > right:
        return 'No'
    else:
        return 'Yes'

print(match_parens(['()(', ')']))
print(match_parens([')', ')']))
print(match_parens(['', ')']))
print(match_parens(['', '(']))
print(match_parens(['(', '(']))