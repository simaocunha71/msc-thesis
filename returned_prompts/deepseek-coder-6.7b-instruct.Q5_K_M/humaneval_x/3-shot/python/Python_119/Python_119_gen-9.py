    def is_good(s):
        c = 0
        for ch in s:
            if ch == '(':
                c += 1
            else:
                if c == 0:
                    return False
                c -= 1
        return c == 0

    return 'Yes' if is_good(lst[0] + lst[1]) else 'No'

