def split_Arr(Arr,n):
    Arr1 = Arr[:n]
    Arr2 = Arr[n:]
    Arr2.extend(Arr1)
    return Arr2