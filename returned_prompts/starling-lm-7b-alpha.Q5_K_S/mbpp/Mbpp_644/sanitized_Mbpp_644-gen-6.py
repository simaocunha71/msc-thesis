def reverse_Array_Upto_K(arr, k):
    left = 0
    right = k
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr