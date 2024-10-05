    def check_paren_balance(s):
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            if depth < 0:
                return False
        return depth == 0

    def get_parens(s):
        depth = 0
        res = []
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                res.append(c)
        return res

    if check_paren_balance(lst[0]) and check_paren_balance(lst[1]):
        return 'Yes'
    elif not check_paren_balance(lst[0]) and not check_paren_balance(lst[1]):
        return 'Yes'

    bal1 = get_parens(lst[0])
    bal2 = get_parens(lst[1][::-1])

    if len(bal1) != len(bal2):
        return 'No'
    else:
        for i, j in zip(bal1, bal2):
            if i != j:
                return 'No'
        return 'Yes'


