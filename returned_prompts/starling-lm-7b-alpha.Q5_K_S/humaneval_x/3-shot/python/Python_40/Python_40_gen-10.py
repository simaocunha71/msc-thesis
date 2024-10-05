    def helper(l, i, acc):
        if i == len(l):
            return False
        if acc == 0:
            return True
        if l[i] in acc:
            return False
        if acc + l[i] in acc:
            return False
        return helper(l, i+1, acc + l[i]) or helper(l, i+1, acc - l[i])

    return helper(l, 0, 0)


