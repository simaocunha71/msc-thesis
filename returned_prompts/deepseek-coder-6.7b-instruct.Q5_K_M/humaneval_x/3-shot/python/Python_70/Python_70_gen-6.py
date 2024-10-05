    lst.sort()
    res = []
    while lst:
        res.append(lst.pop(0))
        if lst:
            res.append(lst.pop())
    return res


