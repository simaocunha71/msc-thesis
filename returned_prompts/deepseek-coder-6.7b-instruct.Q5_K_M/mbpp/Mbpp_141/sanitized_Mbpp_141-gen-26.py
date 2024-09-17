def findMax(arr, n):
    mi = 0
    for i in range(0, n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
def pancake_sort(arr):
    curr_size = len(arr)
    while curr_size > 0:
        mi = findMax(arr, curr_size)
        if mi != curr_size - 1:
            flip(arr, mi)
            flip(arr, curr_size - 1)
        curr_size -= 1
    return arr