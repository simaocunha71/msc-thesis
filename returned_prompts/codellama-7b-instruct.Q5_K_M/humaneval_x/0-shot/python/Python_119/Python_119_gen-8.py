
    def match_parens(lst):
        open_paren = lst[0]
        close_paren = lst[1]
        if open_paren == close_paren:
            return 'No'
        elif open_paren == '(' and close_paren == ')':
            return 'Yes'
        else:
            return 'No'

B:

    def match_parens(lst):
        if lst[0] == ')' or lst[1] == ')':
            return 'No'
        else:
            return 'Yes'

C:

    def match_parens(lst):
        open_paren = lst[0]
        close_paren = lst[1]
        return open_paren == close_paren and open_paren == '('
