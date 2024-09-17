def split_Arr(arr,n):
    if n > len(arr):
        return arr
    else:
        return arr[n:]+arr[:n]