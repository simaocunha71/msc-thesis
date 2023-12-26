
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

    # if len(lst) % 2 != 0:
        # pass
    # else:
        # res = 'Yes' # '(a,b,c)' is good
        # res = 'No' # '(a,b)' is not.
        # return res
    # for paren in lst[::-1]:
        # if (paren[-1]) == '(':
            # paren += 'X' * ((len(lst) - 2 - len(str(paren[-1])) // 2) % 2 + 2)
            # elif (paren[0]) == ')':
                # paren = 'X' * ((len(lst) - 2 - len(str('('))) // 2 + 2) % 2 + 2)
        # if not res: # we couldn't match the last string.
            # return False # we can return false, even if the last string was good. (I don't fully get why?)
    # if lst[::-1][0] in ['(', '+', '-']:
        # match_parens([lst[::-1][0], lst[::-1].replace('+', 'X').replace('-', 'X') + 'X' * ((len(lst) - 3 - len(str(lst[::-1])) // 2 + 2) % 2 + 2), lst