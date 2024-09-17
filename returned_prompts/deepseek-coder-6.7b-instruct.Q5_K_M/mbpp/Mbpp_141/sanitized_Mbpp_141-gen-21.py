def pancake_sort(arr):
    n = len(arr)
    for i in range(n, 0, -1):
        max_index = max_element(arr, i)
        if max_index != i - 1:
            flip(arr, max_index)
            flip(arr, i - 1)
    return arr
def max_element(arr, n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index