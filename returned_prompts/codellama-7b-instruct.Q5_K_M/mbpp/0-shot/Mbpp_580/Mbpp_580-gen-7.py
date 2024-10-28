
def extract_even(t):
    res = []
    for i in t:
        if isinstance(i, tuple):
            res.append(extract_even(i))
        elif i % 2 == 0:
            res.append(i)
    return tuple(res)

