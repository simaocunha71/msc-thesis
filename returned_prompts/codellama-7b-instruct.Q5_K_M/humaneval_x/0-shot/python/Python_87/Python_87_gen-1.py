
def get_row(lst, x):
    lst = [[(i, j) for j, v in enumerate(row) if v == x] for i, row in enumerate(lst)]
    return list(set(sum(lst, [])))
