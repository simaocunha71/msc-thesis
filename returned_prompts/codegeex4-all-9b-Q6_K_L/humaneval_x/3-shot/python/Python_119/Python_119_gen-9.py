    def count_parens(string):
        count = 0
        for c in string:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    return count_parens(lst[0] + lst[1]) or count_parens(lst[1] + lst[0])