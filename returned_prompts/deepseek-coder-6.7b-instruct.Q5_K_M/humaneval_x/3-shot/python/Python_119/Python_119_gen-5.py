    def is_balanced(s):
        while '()' in s:
            s = s.replace('()', '')
        return not s

    return 'Yes' if is_balanced(lst[0] + lst[1]) else 'No'


