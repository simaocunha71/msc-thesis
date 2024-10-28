
def pluck(arr):
    if not arr:
        return []
    arr.sort(key=lambda x: x % 2)
    for i, num in enumerate(arr):
        if num % 2 == 0:
            return [num, i]
    return []


