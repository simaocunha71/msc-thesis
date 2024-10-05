
from itertools import chain, product

def get_row(lst, x):
    rows = []
    for i, row in enumerate(lst):
        cols = []
        for j, col in enumerate(row):
            if col == x:
                cols.append((i, j))
        rows.extend(cols)
    return sorted(rows, key=lambda x: x[0])

print(get_row([[1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]], 1))
