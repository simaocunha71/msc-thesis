
def get_row(lst, x):
    res = []
    for i,row in enumerate(lst):
        for j,val in enumerate(row):
            if val == x:
                res.append((i,j))
    res.sort(key=lambda x: (x[0], -x[1]))
    return res