def split_Arr(Arr, n):
    Arr = Arr[:n] + Arr[n+1:]
    Arr.append(Arr[0])
    Arr.pop(0)
    return Arr
