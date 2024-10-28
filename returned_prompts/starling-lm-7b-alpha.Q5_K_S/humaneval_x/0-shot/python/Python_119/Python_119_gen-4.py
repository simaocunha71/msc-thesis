    # Your code here
    def match_parens(lst):
        open_parentheses = 0
        for i in lst[0]:
            if i == '(':
                open_parentheses += 1
            else:
                if open_parentheses == 0:
                    return 'No'
                else:
                    open_parentheses -= 1
        if open_parentheses == 0:
            for i in lst[1]:
                if i == '(':
                    return 'No'
                else:
                    open_parentheses += 1
            if open_parentheses == 0:
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'

match_parens(['()(', ')']) # 'Yes'
match_parens([')', ')']) # 'No'
match_parens([')', '(']) # 'No'
match_parens(['(', ')']) # 'Yes'
match_parens(['(', '(']) # 'Yes'



























































































































































































































































