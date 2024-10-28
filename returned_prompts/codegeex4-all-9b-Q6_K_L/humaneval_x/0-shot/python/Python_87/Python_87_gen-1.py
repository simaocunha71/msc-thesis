def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                result.append((i, j))
    result.sort()
    return result[::-1]

print(get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

print(get_row([], 1)) == []

print(get_row([[], [1], [1, 2, 3]], 3)) == [(2, 2)]