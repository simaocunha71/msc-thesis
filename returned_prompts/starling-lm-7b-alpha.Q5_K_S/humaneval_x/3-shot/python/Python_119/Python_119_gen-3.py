    def match_parens_helper(s1, s2):
        depth = 0
        for c in s1:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            if depth < 0:
                return False
        depth = 0
        for c in s2:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            if depth < 0:
                return False
        return True

    return 'Yes' if match_parens_helper(lst[0], lst[1]) or match_parens_helper(lst[1], lst[0]) else 'No'


