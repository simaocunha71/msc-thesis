def reverse_Array_Upto_K(arr, K):
    for i in range(K//2):
        arr[i], arr[K-i-1] = arr[K-i-1], arr[i]
    return arr