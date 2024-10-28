
def pluck(arr):
    if len(arr) == 0:
        return []
    min_even = 10000
    index = -1
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < min_even:
            min_even = arr[i]
            index = i
    return [min_even, index]
