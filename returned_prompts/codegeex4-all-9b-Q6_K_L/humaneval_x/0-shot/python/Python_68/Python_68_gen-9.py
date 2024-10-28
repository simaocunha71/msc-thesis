def pluck(arr):
    if not arr:
        return []
    evens = sorted([(x, i) for i, x in enumerate(arr) if x % 2 == 0])
    if evens:
        return evens[0]
    return []

print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]