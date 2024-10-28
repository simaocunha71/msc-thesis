    def match_parens(lst):
        lst1, lst2 = lst
        open_count = 0
        for c in lst1:
            if c == '(':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return 'No'
        for c in lst2:
            if c == '(':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return 'No'
        return 'Yes'


