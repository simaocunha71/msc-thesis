def reverse_Array_Upto_K(arr, k):
    # Firstly, we will reverse the first k elements.
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1
    return arr