    def match_parens_aux(lst):
        count = 0
        for c in lst:
            if c == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    return 'Yes' if match_parens_aux(lst[0]) or match_parens_aux(lst[1]) else 'No'


