    def check_parens(s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1

            if count < 0:
                return False
        return count == 0

    return check_parens(lst[0] + lst[1]) or check_parens(lst[1] + lst[0])

