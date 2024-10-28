
def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        for j, n in enumerate(row):
            if n == x:
                res.append((i, j))
    return sorted(res, key=lambda x: (x[0], -x[1]))
