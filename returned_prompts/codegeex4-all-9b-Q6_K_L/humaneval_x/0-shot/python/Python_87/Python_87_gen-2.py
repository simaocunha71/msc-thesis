def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    result.sort(key=lambda v: (v[0], -v[1]))
    return result

print(get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)) # == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1)) # == []
print(get_row([[], [1], [1, 2, 3]], 3)) # == [(2, 2)]