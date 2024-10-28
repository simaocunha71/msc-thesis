    def helper(l, idx, acc):
        if idx == len(l):
            return False
        if l[idx] + acc in l:
            return True
        return helper(l, idx + 1, acc + l[idx])
    return helper(l, 0, 0)


