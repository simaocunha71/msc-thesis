def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result

print(get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1))

print(get_row([], 1))

print(get_row([[], [1], [1, 2, 3]], 3))