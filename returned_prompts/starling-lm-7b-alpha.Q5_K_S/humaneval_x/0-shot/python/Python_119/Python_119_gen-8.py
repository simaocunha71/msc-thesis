    # Your code here
    def match_parens(lst):
        string = lst[0] + lst[1]
        count = 0
        for i in string:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
                if count < 0:
                    return 'No'
        if count == 0:
            return 'Yes'
        else:
            return 'No'

match_parens(['()(', ')']) # 'Yes'
match_parens([')(', ')']) # 'No'


def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
   