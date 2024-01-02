
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''

    for i in range(len(lst)):
        if lst[i] != ',':
            count = 0
            while lst[count] != ',':
                #print lst[count],end=' '
                count +=1
                if lst[count] == '(':
                    count +=1
                    if lst[count+1] == ')' and lst[count-1] == '(':
                        pass
                    else:
                        return False
                elif lst[count] == ')':
                    print True,end=' '
                    break
            #print count - 1 ,end='\n'
            if count - 1 != len(lst):
                return False
    return True
