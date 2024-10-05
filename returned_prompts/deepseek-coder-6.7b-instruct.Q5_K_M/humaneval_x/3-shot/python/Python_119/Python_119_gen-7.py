    def is_balanced(s):
        c = 0
        for ch in s:
            if ch == '(':
                c += 1
            elif ch == ')':
                c -= 1
            if c < 0:
                return False
        return c == 0

    s1, s2 = lst
    return 'Yes' if is_balanced(s1 + s2) else 'No'


