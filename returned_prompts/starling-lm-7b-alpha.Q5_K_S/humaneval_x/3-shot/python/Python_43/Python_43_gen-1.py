    def helper(l, i, s):
        if i == len(l) - 1:
            if s == 0:
                return True
            else:
                return False
        if l[i + 1] == -l[i]:
            if helper(l, i + 1, s):
                return True
        if l[i] + l[i + 1] == 0:
            return helper(l, i + 1, s + l[i + 1])
        if l[i] + l[i + 1] == 0:
            return helper(l, i + 1, s + l[i + 1])
        return helper(l, i + 1, s)

    return helper(l, 0, 0)


