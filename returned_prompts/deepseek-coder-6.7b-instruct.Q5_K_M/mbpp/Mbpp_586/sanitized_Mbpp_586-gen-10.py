def split_Arr(arr,n):
    arr[:] = arr[n:] + arr[:n]
    return arr