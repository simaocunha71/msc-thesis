    def helper(l):
        if len(l) % 3 == 0:
            return l
        else:
            return helper(l[:-1]) + helper(l[-1:])
    return helper(l)


