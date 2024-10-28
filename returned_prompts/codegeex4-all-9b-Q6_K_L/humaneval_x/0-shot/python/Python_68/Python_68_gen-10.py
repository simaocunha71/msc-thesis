def pluck(arr):
    if not arr: return []
    even = [i for i in arr if i % 2 == 0]
    if not even: return []
    min_even = min(even)
    return [min_even, arr.index(min_even)]

print(pluck([4,2,3])) # [2, 1]
print(pluck([1,2,3])) # [2, 1]
print(pluck([])) # []
print(pluck([5, 0, 3, 0, 4, 2])) # [0, 1]