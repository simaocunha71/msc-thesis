
    def match_parens(lst):
        s1, s2 = lst
        if s1.count('(') < s1.count(')') or s2.count('(') > s2.count(')'):
            return 'No'
        if s1.count('(') > s1.count(')') or s2.count('(') < s2.count(')'):
            return 'No'
        if s1.count('(') + s2.count('(') < s1.count(')') + s2.count(')'):
            return 'No'
        if s1.count('(') + s2.count('(') > s1.count(')') + s2.count(')'):
            return 'No'
        return 'Yes'

print(match_parens(['()(', ')']))
print(match_parens([')', ')']))

# The function checks if the number of opening and closing parentheses are equal in both strings,
# and if the total number of parentheses in both strings is balanced. If all these conditions are met,
# it returns 'Yes'. Otherwise, it returns 'No'.

'''
