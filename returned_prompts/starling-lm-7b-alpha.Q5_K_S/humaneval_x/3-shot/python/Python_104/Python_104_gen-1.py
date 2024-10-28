    def is_odd(n):
        return all(d % 2 == 1 for d in str(n))

    res = []
    for elem in x:
        if is_odd(elem):
            res.append(elem)
    return sorted(res)


