
def pluck(arr):
    res = []
    for i, v in enumerate(arr):
        if v % 2 == 0:
            res.append([v, i])
    if not res:
        return []
    return sorted(res, key=lambda x: x[0])[0]

print(pluck([5, 0, 3, 0, 4, 2]))
print(pluck([4, 2, 3]))
print(pluck([1,2,3]))
print(pluck([]))