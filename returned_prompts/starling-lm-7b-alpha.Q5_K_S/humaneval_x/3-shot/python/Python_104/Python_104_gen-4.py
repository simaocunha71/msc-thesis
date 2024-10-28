    def helper(x):
        if x == 0:
            return []
        res = []
        for d in helper(x // 10):
            if d % 2 == 0:
                continue
            res.append(d)
        if x % 10 % 2 == 0:
            return res
        else:
            res.append(x % 10)
            return res
    res = []
    for x in x:
        for d in helper(x):
            if d not in res:
                res.append(d)
    res.sort()
    return res




