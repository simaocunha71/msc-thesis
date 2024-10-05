    def helper(s, depth=0):
        if depth < 0:
            return False
        if depth == 0 and s == '':
            return True
        if s[-1] == '(':
            return helper(s[:-1], depth + 1)
        if s[-1] == ')':
            return helper(s[:-1], depth - 1)
        return False

    return 'Yes' if helper(lst[0]) or helper(lst[1]) else 'No'


