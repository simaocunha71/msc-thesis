def split_Arr(arr,n):
    arr[:n] = arr[n:] + arr[:n]
    return arr