
def get_row(lst, x):
    result = []
    for index, i in enumerate(lst):
        if x in i:
            result.append((index, i.index(x)))
    result = sorted(result, key=lambda x: x[0])
    for index, i in enumerate(result):
        result[index] = (i[0], len(lst[i[0]]) - i[1] - 1)
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result

# testing
print(get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1) == [])
print(get_row([[], [1], [1, 2, 3]], 3) == [(1, 2)])
print(get_row([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 3) == [(2, 2)])















































































































































































