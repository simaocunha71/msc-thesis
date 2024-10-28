    def helper(l, i, acc):
        if i >= len(l):
            return acc
        if acc + l[i] == 0 and i > len(l) - 3:
            return True
        return helper(l, i + 1, acc + l[i]) if i < len(l) - 2 else False
    return helper(l, 0, 0)


