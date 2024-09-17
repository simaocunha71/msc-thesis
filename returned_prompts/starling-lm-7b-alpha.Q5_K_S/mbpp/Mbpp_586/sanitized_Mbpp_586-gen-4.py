def split_Arr(arr,n):
    if(len(arr) <= n):
        return arr
    else:
        return arr[n:] + arr[:n]