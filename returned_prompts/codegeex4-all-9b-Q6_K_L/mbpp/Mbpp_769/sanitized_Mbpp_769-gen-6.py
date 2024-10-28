def Diff(first, second):
    res = []
    for i in first:
        if i not in second:
            res.append(i)
    return res