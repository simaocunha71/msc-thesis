    n = len(arr)
    if n == 0:
        return True
    
    last = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] > last:
            return False
        last = arr[i]
    return True


