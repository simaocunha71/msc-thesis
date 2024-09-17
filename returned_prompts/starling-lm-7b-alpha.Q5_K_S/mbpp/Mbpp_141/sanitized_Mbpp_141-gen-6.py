def pancake_sort(a):
    res = []
    while len(a) > 1:
        max_i = a.index(max(a))
        res.append(max_i)
        a.pop(max_i)
        a.insert(0, max(a))
        a.pop(max_i)
    res.append(a[0])
    return res