def reverse_Array_Upto_K(arr, k):
    l = len(arr)
    for i in range(k):
        arr[i], arr[l - i - 1] = arr[l - i - 1], arr[i]
    return arr