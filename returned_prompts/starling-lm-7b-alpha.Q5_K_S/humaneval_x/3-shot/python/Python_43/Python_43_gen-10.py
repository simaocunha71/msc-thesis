    def helper(l, idx):
        if idx < 0:
            return False
        if l[idx] + l[len(l) - 1] == 0:
            return True
        if l[idx] + l[len(l) - 1] < 0:
            return helper(l, idx - 1)
        return helper(l, idx - 1)

    return helper(l, len(l) - 1)


