
def by_length(arr):
    arr = [x for x in arr if 1 <= x <= 9]
    arr.sort(reverse=True)
    arr = [str(x) for x in arr]
    arr = [x.capitalize() for x in arr]
    return arr

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))



