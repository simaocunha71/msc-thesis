
    def match_parens(lst):
        s1, s2 = lst
        stack = []
        for c in s1 + s2:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return 'No'
                stack.pop()
        return 'Yes' if not stack else 'No'

    print(match_parens(['()(', ')']))
    print(match_parens([')', ')']))
    print(match_parens(['(', ')']))