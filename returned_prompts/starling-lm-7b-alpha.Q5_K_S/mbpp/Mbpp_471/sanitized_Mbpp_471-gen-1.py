def find_remainder(arr,n):
    if len(arr) == 1:
        return arr[0] % n
    else:
        if len(arr)%2 == 0:
            return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n)) % n
        else:
            return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n) * arr[-1]) % n