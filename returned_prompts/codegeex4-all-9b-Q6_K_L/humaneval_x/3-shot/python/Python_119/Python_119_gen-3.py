    def count_parens(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count

    s1, s2 = lst
    if count_parens(s1 + s2) == 0:
        return 'Yes'
    elif count_parens(s1 + s2) == count_parens(s1) or count_parens(s1 + s2) == count_parens(s2):
        return 'Yes'
    else:
        return 'No'